import copy
movie_pran=['롯데시네마','CGV']
movie_dict={'all': None,'롯데시네마' : None, 'CGV': None}

convenience_pran=['CU','GS25','세븐일레븐','미니스톱']
convenience_dict={'all' : None, 'CU' : None, 'GS25' : None, '세븐일레븐':None, '미니스톱':None}

defalt_dict={'telecom': None,'movie': copy.deepcopy(movie_dict),'convenience': copy.deepcopy(convenience_dict),
             'transit': None}
