#!/usr/bin/env python
import os
import sys

import xmlrpclib

server = xmlrpclib.ServerProxy('https://api.webfaction.com/')


def login(user, password):
    return server.login(user, password)


def create_doamin():
    domain = raw_input("Enter Domain Name")
    subdomain = raw_input("Enter Sub Domain Name Leave Blank if no subdoamin")
    if subdomain != '':
        server.create_domain(
            session_id, domain, 'www')
        server.create_domain(
            session_id,
            'www.{0}'.format(domain), 'www', 'www.{0}'.format(subdomain)
        )
    else:
        server.create_domain(
            session_id, domain, 'www', subdomain)
        server.create_domain(
            session_id,
            'www.{0}'.format(domain), 'www', 'www.{0}'.format(subdomain)
        )


if __name__ == "__main__":
    user = raw_input("Enter UserName")
    password = raw_input("Enter Password")
    session_id, account = login(user, password)
    create_doamin()
