#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
from ConfigParser import ConfigParser
from logging import getLogger, basicConfig
from StringIO import StringIO
import os
import outbox
import shutil
import subprocess
import sys
import tarfile
import urllib

basicConfig()
logger = getLogger(__name__)


class Export(object):

    def __init__(self, config):
        self.getters = defaultdict(lambda:config.get)
        self.getters['mail_port'] = config.getint

    def getConfig(self, key):
        try:
            return self.getters[key]('gs_export', key)
        except ConfigParser, e:
            logger.error('You did not fully define your configuration (%s)'
                         , str(e))
            raise

    def sendmail(self, msg):
        c = self.getConfig
        with outbox.Outbox(username=c('mail_user'),
                           password=c('mail_password'),
                           server=c('mail_server'), port=c('mail_port'
                           ), mode=c('mail_mode')) as obox:
            obox.username = c('mail_from')
            obox.send(outbox.Email(subject='GS Profile needs action: %s/manage_main'
                       % c('base_url'), body=msg,
                      recipients=[c('mail_recipient')]))

    def __call__(self):
        c = self.getConfig
        urlob = urllib.urlopen(c('base_url'),
                               urllib.urlencode({'manage_exportAllSteps:method': ' Export all steps '
                               , '__ac_name': c('user'),
                               '__ac_password': c('password')}))
        try:
            tarob = tarfile.open(fileobj=StringIO(urlob.read()))
        except tarfile.ReadError, e:
            self.sendmail(str(e)
                          + ' Maybe the server is down, or the credentials are wrong'
                          )
            sys.exit(1)

        path = c('path')
        tarob.extractall(path)
        curdir = os.getcwd()
        try:
            create_git_repo = not os.path.exists(path + '/.git')
            os.chdir(path)
            for ignore in c('ignore').split():
                try:
                    os.remove(ignore)
                except OSError:
                    shutil.rmtree(ignore)
            if create_git_repo:
                subprocess.call(['git', 'init'])
            result = subprocess.check_output(['git', 'status', '-s'])
            if result:
                self.sendmail(result)
        finally:
            os.chdir(curdir)


def main():
    config = ConfigParser()
    try:
        config.read(sys.argv[1])
    except Exception, e:
        logger.error('You must provide an absolute path to a configuration file! (%s)'
                     , str(e))
        raise
    Export(config)()
