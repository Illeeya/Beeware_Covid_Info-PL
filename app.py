import toga as t
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from urllib import request
from json import loads

class CovidInfo(t.App):

    def startup(self):
        
        main_box = t.Box(style=Pack(direction= COLUMN))

        url1 = "http://api.worldbank.org/v2/country/PL/indicator/SP.POP.TOTL/?date=2019&format=JSON"
        url2 = "https://coronavirus-19-api.herokuapp.com/countries/poland"

        try: 
            response_people = request.urlopen(url1).read()
            response_covid  = request.urlopen(url2).read()
        except ConnectionError:
            err_msg = "There was a connection error."
            error_lbl = t.Label(err_msg)
            error_lbl.style.update(padding = 30)
            main_box.add(error_lbl)
        except Exception as e:    
            err_msg = f"An error occured. Error type: {type(e)}"
            error_lbl = t.Label(err_msg)
            error_lbl.style.update(padding = 30)
            main_box.add(error_lbl)
        else:

            response_people = response_people.decode()
            response_covid = response_covid.decode()

            response_people = loads(response_people)
            response_covid = loads(response_covid)



            #------------------------------------------------------------------------------------------------
            #DATA

                #COVID DATA
            cases = response_covid['cases']
            todayCases = response_covid['todayCases']

            deaths = response_covid['deaths']
            todayDeaths = response_covid['todayDeaths']

            recovered = response_covid['recovered']
            population = response_people[1][0]["value"]

            sick_percentage = round(response_covid["cases"] * 100 / population, 2)
            dead_percentage = round(response_covid["deaths"] * 100 / population, 2)

            #------------------------------------------------------------------------------------------------
            #BOXES
            covid_box = t.Box(style=Pack(direction= COLUMN, padding = 10))

                #COVID BOX
                    #Title
            cb01 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            brk1 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
                    #Populacja
            cb10 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb11 = t.Box(style=Pack(direction= ROW, padding_bottom = 20))
                    #Zarazen
            cb20 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb21 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb22 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb23 = t.Box(style=Pack(direction= ROW, padding_bottom = 20))
                    #Zarazen
            cb30 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb31 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb32 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb33 = t.Box(style=Pack(direction= ROW, padding_bottom = 20))
                    #Populacja
            cb40 = t.Box(style=Pack(direction= ROW, padding_bottom = 10))
            cb41 = t.Box(style=Pack(direction= ROW, padding_bottom = 20))



            #------------------------------------------------------------------------------------------------
            #ELEMENTS
                #COVID BOX
                    #Title
            clbl_001 = t.Label('\U0001F4A9 COVID INFO \U0001F4A9',                          style=Pack(width = 400,  font_size = 15, font_weight = 'bold', text_align = 'left'))
            brk_001  = t.Label('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -',style=Pack(width = 400, font_size = 12, text_align = 'left'))
                    
                    #Populacja
            clbl_101 = t.Label('\U0001F464',                                                style=Pack(width = 25,  font_size = 12, text_align = 'left'))
            clbl_102 = t.Label('Populacja',                                                 style=Pack(width = 375, font_size = 12, text_align = 'left'))
            
            clbl_111 = t.Label('Łącznie',                                                   style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_112 = t.Label(f"{population:,}".format(population).replace(',',' '),       style=Pack(width = 150, font_size = 12,  text_align = 'right'))
                    
                    #Zarazen
            clbl_201 = t.Label('\U0001F922',                                                style=Pack(width = 25,  font_size = 12, text_align = 'left'))
            clbl_202 = t.Label('Zarażeń',                                                   style=Pack(width = 375, font_size = 12, text_align = 'left'))
           
            clbl_211 = t.Label("Łącznie",                                                   style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_212 = t.Label(f"{cases:,}".format(cases).replace(',',' '),                 style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            
            clbl_221 = t.Label("Dzisiaj",                                                   style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_222 = t.Label(f"+{todayCases:,}".format(todayCases).replace(',',' '),      style=Pack(width = 150, font_size = 12,  text_align = 'right'))

            clbl_231 = t.Label("% pop",                                                     style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_232 = t.Label(f"{sick_percentage} %",                                      style=Pack(width = 167, font_size = 12,  text_align = 'right'))
                    
                    #Zgonow
            clbl_301 = t.Label('\U0001F480',                                                style=Pack(width = 25,  font_size = 12, text_align = 'left'))
            clbl_302 = t.Label('Zmarłych',                                                  style=Pack(width = 375, font_size = 12, text_align = 'left'))
           
            clbl_311 = t.Label("Łącznie",                                                   style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_312 = t.Label(f"{deaths:,}".format(deaths).replace(',',' '),               style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            
            clbl_321 = t.Label("Dzisiaj",                                                   style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_322 = t.Label(f"+{todayDeaths:,}".format(todayDeaths).replace(',',' '),    style=Pack(width = 150, font_size = 12,  text_align = 'right'))

            clbl_331 = t.Label("% pop",                                                     style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_332 = t.Label(f"{dead_percentage} %",                                      style=Pack(width = 167, font_size = 12,  text_align = 'right'))
                     
                    #Wyleczeni
            clbl_401 = t.Label('\U0001F49E',                                                style=Pack(width = 25,  font_size = 12, text_align = 'left'))
            clbl_402 = t.Label('Wyleczonych',                                               style=Pack(width = 375, font_size = 12, text_align = 'left'))
            
            clbl_411 = t.Label('Łącznie',                                                   style=Pack(width = 150, font_size = 12,  text_align = 'right'))
            clbl_412 = t.Label(f"{recovered:,}".format(recovered).replace(',',' '),         style=Pack(width = 150, font_size = 12,  text_align = 'right'))
                                      

        #------------------------------------------------------------------------------------------------
        # INSERTING ELEMENTS

            # Elements to boxes
                #Covid Box
                    # Title
        cb01.add(clbl_001)
        brk1.add(brk_001)
                    # Populacja
        cb10.add(clbl_101)
        cb10.add(clbl_102)

        cb11.add(clbl_111)
        cb11.add(clbl_112)
                    # Zarazen
        cb20.add(clbl_201)
        cb20.add(clbl_202)

        cb21.add(clbl_211)
        cb21.add(clbl_212)

        cb22.add(clbl_221)
        cb22.add(clbl_222)

        cb23.add(clbl_231)
        cb23.add(clbl_232)
                    # Smierci
        cb30.add(clbl_301)
        cb30.add(clbl_302)

        cb31.add(clbl_311)
        cb31.add(clbl_312)

        cb32.add(clbl_321)
        cb32.add(clbl_322)

        cb33.add(clbl_331)
        cb33.add(clbl_332)
                    # Wyleczonych
        cb40.add(clbl_401)
        cb40.add(clbl_402)

        cb41.add(clbl_411)
        cb41.add(clbl_412)


            # Boxes to boxes
        covid_box.add(cb01)
        covid_box.add(brk1)
        covid_box.add(cb10)
        covid_box.add(cb11)
        covid_box.add(cb20)
        covid_box.add(cb21)
        covid_box.add(cb22)
        covid_box.add(cb23)
        covid_box.add(cb30)
        covid_box.add(cb31)
        covid_box.add(cb32)
        covid_box.add(cb33)
        covid_box.add(cb40)
        covid_box.add(cb41)

            # Boxes to main
        main_box.add(covid_box)

        #------------------------------------------------------------------------------------------------
        self.main_window = t.MainWindow(title='CovidInfo')
        self.main_window.size = (400, 500)
        self.main_window.content = main_box
        self.main_window.show()

def main():
    return CovidInfo()
