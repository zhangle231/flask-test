menus = {'name':'1 test','is_leaf':0,
           'children':[
                    {'name':'1.1 test','is_leaf':1,'children':None},
                    {'name':'1.2 test','is_leaf':0,
                     'children':[
                            {'name':'1.2.1 test','is_leaf':0,'children':[
                                    {'name':'1.2.1.1 test','is_leaf':0,'children':[
                                        {'name':'1.2.1.1.1 test','is_leaf':0,'children':[
                                            {'name':'1.1 test','is_leaf':1,'children':None},
                                        ]},
                                    ]},
                            ]}
                        ]}
            ]
}

src = [
        {"name":"root","pid":"0","id":"1"},
        {"name":"0010","pid":"1","id":"2"},
        {"name":"0020","pid":"1","id":"3"},
        {"name":"0011","pid":"2","id":"4"},
        {"name":"0030","pid":"1","id":"5"},
        {"name":"0031","pid":"5","id":"6"},
        {"name":"0021","pid":"3","id":"7"},
        {"name":"0022","pid":"3","id":"8"},
        {"name":"0012","pid":"2","id":"9"},
]
 
[ print(x) for x in src ]


