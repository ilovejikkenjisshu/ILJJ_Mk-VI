# -*- coding: utf-8 -*-

from iljjmkvi import ILJJ_Mk_VI
import pytoml


def main():
    with open('./settings.toml') as f:
        settings = pytoml.load(f)

    client = ILJJ_Mk_VI(settings)
    client.run(settings['general']['token'])

if __name__ == '__main__':
    main()

