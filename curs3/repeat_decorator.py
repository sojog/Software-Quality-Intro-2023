



def decoratorator_executa_de_3_ori(func):
    def wrapper_function(string):
       for i in range(10):
           func(string)
    return wrapper_function


@decoratorator_executa_de_3_ori
def no_of_characters(string):
    no_of_ch = len(string) 
    print('sunt ', no_of_ch, 'caracter in cuvant')


no_of_characters('hello world!')