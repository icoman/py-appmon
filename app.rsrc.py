{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgTemplate',
          'title':'Standard Template with File->Exit menu',
          'size':(557, 384),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'TextArea', 
    'name':'envinfo', 
    'position':(20, 120), 
    'size':(500, 190), 
    'text':'envinfo', 
    },

{'type':'StaticText', 
    'name':'titluapp', 
    'position':(20, 40), 
    'font':{'faceName': u'Segoe UI', 'family': 'sansSerif', 'size': 24}, 
    'text':'titluapp', 
    },

{'type':'StaticText', 
    'name':'textceas', 
    'position':(400, 0), 
    'size':(142, 37), 
    'alignment':'right', 
    'font':{'faceName': u'Segoe UI', 'family': 'sansSerif', 'size': 18}, 
    'text':'textceas', 
    },

{'type':'Button', 
    'name':'Close', 
    'position':(440, 60), 
    'command':'iesire', 
    'label':'Close', 
    },

] # end components
} # end background
] # end backgrounds
} }
