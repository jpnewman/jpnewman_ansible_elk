
ARTIFACTORY_NUGET_API_PREFIX = '/artifactory/api/nuget/'

NUGET_REPOS = [
    'LIBS',
    'DEPLOY',
    'NUGET_ORG'
]

HTTP_METHODS = [
    'GET',
    'POST',
    'PUT'
]

REQUEST_TYPE = [
    'ACCEPTED DEPLOY',
    'ACCEPTED DOWNLOAD',
    'DENIED DEPLOY',
    'DENIED ANNOTATE',
    'DENIED DELETE'
]

NUGET_PACKAGES = {
    'EntityFramework': {
        'versions': [
            '6.1.3',
            '6.1.3-beta1',
            '6.1.2',
            '6.1.2-beta2',
            '6.1.2-beta1',
            '6.1.1',
            '6.1.1-beta1',
            '6.1.0',
            '6.1.0-beta1',
            '6.1.0-alpha1',
            '6.0.2',
            '6.0.2-beta1',
            '6.0.1',
            '6.0.0',
            '6.0.0-rc1',
            '6.0.0-beta1',
            '6.0.0-alpha3',
            '6.0.0-alpha2',
            '6.0.0-alpha1',
            '5.0.0',
            '5.0.0-rc',
            '5.0.0-beta2',
            '5.0.0-beta1',
            '4.3.1',
            '4.3.0',
            '4.3.0-beta1',
            '4.2.0',
            '4.1.10715',
            '4.1.10331',
            '4.1.10311'
        ]
    },
    'Newtonsoft.Json': {
        'versions': [
            '10.0.2',
            '10.0.1',
            '9.0.1',
            '8.0.3',
            '8.0.2',
            '8.0.1',
            '7.0.1',
            '6.0.8',
            '6.0.7',
            '6.0.6',
            '6.0.5',
            '6.0.4',
            '6.0.3',
            '6.0.2',
            '6.0.1',
            '5.0.8',
            '5.0.7',
            '5.0.6',
            '5.0.5',
            '5.0.4',
            '5.0.3',
            '5.0.2',
            '5.0.1',
            '4.5.11',
            '4.5.10',
            '4.5.9',
            '4.5.8',
            '4.5.7',
            '4.5.6',
            '4.5.5',
            '4.5.4',
            '4.5.3',
            '4.5.2',
            '4.5.1',
            '4.0.8',
            '4.0.7',
            '4.0.6',
            '4.0.5',
            '4.0.4',
            '4.0.3',
            '4.0.2',
            '4.0.1',
            '3.5.8'
        ]
    },
    'NUnit': {
        'versions': [
            '3.6.1',
            '3.6.0',
            '3.5.0',
            '3.4.1',
            '3.4.0',
            '3.2.1',
            '3.2.0',
            '3.0.1',
            '3.0.0',
            '3.0.0-rc-3',
            '3.0.0-rc-2',
            '3.0.0-rc',
            '3.0.0-beta-5',
            '3.0.0-beta-4',
            '3.0.0-beta-3',
            '3.0.0-beta-2',
            '3.0.0-beta-1',
            '3.0.0-alpha-5',
            '3.0.0-alpha-4',
            '3.0.0-alpha-3',
            '3.0.0-alpha-2',
            '3.0.0-alpha',
            '2.6.4',
            '2.6.3',
            '2.6.2',
            '2.6.1',
            '2.6.0.12054',
            '2.5.10.11092',
            '2.5.9.10348',
            '2.5.7.10213'
        ]
    },
    'jQuery': {
        'versions': [
            '3.1.1',
            '3.1.0',
            '3.0.0.1',
            '3.0.0',
            '2.2.4',
            '2.2.3',
            '2.2.2',
            '2.2.1',
            '2.2.0',
            '2.1.4',
            '2.1.3',
            '2.1.2',
            '2.1.1',
            '2.1.0',
            '2.0.3',
            '2.0.2',
            '2.0.1.1',
            '2.0.1',
            '2.0.0',
            '1.12.4',
            '1.12.3',
            '1.12.2',
            '1.12.1',
            '1.12.0',
            '1.11.3',
            '1.11.2',
            '1.11.1',
            '1.11.0',
            '1.10.2',
            '1.10.1',
            '1.10.0.1',
            '1.10.0',
            '1.9.1',
            '1.9.0',
            '1.8.3',
            '1.8.2',
            '1.8.1',
            '1.8.0',
            '1.7.2',
            '1.7.1.1',
            '1.7.1',
            '1.7.0',
            '1.6.4',
            '1.6.3',
            '1.6.2',
            '1.6.1',
            '1.6.0',
            '1.5.2',
            '1.5.1',
            '1.5.0',
            '1.4.4',
            '1.4.3',
            '1.4.2',
            '1.4.1'
        ]
    },
    'log4net': {
        'versions': [
            '2.0.8',
            '2.0.7',
            '2.0.6',
            '2.0.5',
            '1.2.15',
            '2.0.4',
            '1.2.14',
            '2.0.3',
            '1.2.13',
            '2.0.2',
            '1.2.12',
            '2.0.1',
            '1.2.12',
            '2.0.0',
            '1.2.11',
            '1.2.10'
        ]
    },
    'AutoMapper': {
        'versions': [
            '6.0.2',
            '5.2.0',
            '5.1.1',
            '5.0.2',
            '5.0.0-beta-1',
            '4.2.1',
            '4.2.0',
            '4.1.1',
            '4.0.4',
            '4.0.0-alpha1',
            '3.3.1',
            '3.3.0',
            '3.2.1',
            '3.1.1',
            '3.1.0',
            '3.0.0',
            '2.2.1',
            '2.2.0',
            '2.1.267',
            '2.1.266',
            '2.1.265',
            '2.1.262',
            '2.1.1',
            '2.0.0',
            '1.1.2',
            '1.1.0.118'
        ]
    }
}
