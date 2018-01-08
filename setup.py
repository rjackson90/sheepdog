from setuptools import setup

setup(
    name='sheepdog',
    version='0.2.0',
    description='Flask blueprint for herding data submissions',
    url='https://github.com/uc-cdis/sheepdog',
    license='Apache',
    packages=[
        'sheepdog',
        'sheepdog.auth',
        'sheepdog.blueprint',
        'sheepdog.blueprint.routes',
        'sheepdog.blueprint.routes.views',
        'sheepdog.blueprint.routes.views.program',
        'sheepdog.transactions',
        'sheepdog.transactions.close',
        'sheepdog.transactions.deletion',
        'sheepdog.transactions.release',
        'sheepdog.transactions.review',
        'sheepdog.transactions.submission',
        'sheepdog.transactions.upload',
        'sheepdog.utils',
        'sheepdog.utils.transforms',
    ],
    install_requires=[
        'boto==2.36.0',
        'cryptography==2.0.3',
        'Flask-Cors==1.9.0',
        'Flask-SQLAlchemy-Session==1.1',
        'Flask==0.10.1',
        'fuzzywuzzy==0.6.1',
        'graphene==0.10.2',
        'jsonschema==2.5.1',
        'lxml==3.8.0',
        'psycopg2==2.7.3.2',
        'PyYAML==3.11',
        'requests==2.5.2',
        'setuptools==30.1.0',
        'simplejson==3.8.1',
        'sqlalchemy==0.9.9',
        'psqlgraph',
        'userdatamodel',
        'cdisutils',
        'cdis_oauth2client',
        'gdcdictionary',
        'gdcdatamodel',
    ],
    dependency_links=[
        'git+https://git@github.com/NCI-GDC/psqlgraph.git@7b5de7d56aa3159a9526940eb273579ddbf084ca#egg=psqlgraph',
        'git+https://git@github.com/uc-cdis/cdis-python-utils.git@0.1.5#egg=cdispyutils',
        'git+https://git@github.com/uc-cdis/userdatamodel.git@f25f5dfb356e80c45153ffd3e91b399be672a81c#egg=userdatamodel',
        'git+https://git@github.com/uc-cdis/cdis_oauth2client.git@0.1.1#egg=cdis_oauth2client',
        'git+https://git@github.com/NCI-GDC/cdisutils.git@a79409a0ce5071a81c6997d4ed1549c3544fbdcd#egg=cdisutils',
        'git+https://git@github.com/uc-cdis/datadictionary.git@0.1.1#egg=gdcdictionary',
        'git+https://git@github.com/NCI-GDC/gdcdatamodel.git@755c6d7c380b69dc36dced55700bc9e24a084db1#egg=gdcdatamodel',
        'git+https://git@github.com/NCI-GDC/signpost.git@c5d499936943e71eefe2ec4b3d4ced6ac48f35c0#egg=signpost',
        'git+https://git@github.com/uc-cdis/indexclient.git@d49134f4626b69a8ef02c189ed0047ad1a635cb0#egg=indexclient',
        'git+https://git@github.com/uc-cdis/dictionaryutils.git@35899a878381eeb8ba91fd9124d285809d0063e8#egg=dictionaryutils',
    ],
)
