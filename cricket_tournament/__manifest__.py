{
    'name': "Live Cricket Score Board",

    'summary': """cricket tournament""",
    'author': "Vivek Tiwari",
    'depends':["web_dashboard"],
    'version': '0.1',
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/cricket.xml',
        'views/wizard.xml',
        'views/templates.xml',

        'report/report.xml'
    ],
    'demo':[
        'demo/demo.xml'
    ],
}


