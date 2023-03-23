from main import convert_number,add_numbers,subtract_numbers,\
divide_numbers,rem_numbers,multiply_numbers

def out_green(text):
    print("\033[32m{}".format(text))

#Case of convertation number: function must return converted number from 10 count system
#To another what he choose. 
#Exception will be output if count system doesnt equals : 2,8,10,16
def test_convert():
    assert convert_number(10,10) == '10'
    assert convert_number(10,2) == '1010'
    assert convert_number(10,8) == '12'
    assert convert_number(15,16) == 'F'
    assert convert_number(10,17) == 'Base 17 out of range!'
    

#Case of testing sum: function must return sum of two values on input count system
#If count system went out of range, will be output of exception 
def test_sum():
    assert add_numbers('1010','1010',2) == '10100'
    assert add_numbers('32','16',8) == '50'
    assert add_numbers('10','10',10) == '20'
    assert add_numbers('66','66',16) == 'CC'
    assert add_numbers('10','2',2) == 'Number 10 or 2 isnt availabe in this count system!'
    assert add_numbers('8','10',8) == 'Number 8 or 10 isnt availabe in this count system!'
    assert add_numbers('-10','10',10) == '0'
    assert add_numbers('16','6',16) == '1C'
    assert add_numbers('10','10',17) == 'Base 17 out of range!'
   


#Case of subtraction numbers: function must return subtraction of two numbers 
#on input count system. 
#If count system went out of range, will be output of exception 
def test_sub():
    assert subtract_numbers('1010','10',2) == '1000'
    assert subtract_numbers('512','65',8) == '425'
    assert subtract_numbers('1000','7',10) == '993'
    assert subtract_numbers('ABC','A',16) == 'AB2'
    assert subtract_numbers('-100','-100',10) == '0'
    assert subtract_numbers('10','2',2) == 'Number 10 or 2 isnt availabe in this count system!'
    assert subtract_numbers('1','1',691) == 'Base 691 out of range!'


#Case of multiply numbers: function must return multiply of two numbers
#on input count system. 
#If count system went out of range, will be output of exception
def test_mul():
    assert multiply_numbers('10','10',2) == '100'
    assert multiply_numbers('10','10',8) == '100' 
    assert multiply_numbers('10','10',10) == '100'
    assert multiply_numbers('10','10',16) == '100'
    assert multiply_numbers('10','2',2) == 'Number 10 or 2 isnt availabe in this count system!'
    assert multiply_numbers('10','10',592349529) == 'Base 592349529 out of range!'
    assert multiply_numbers('1','0',10) == '0'


#Case of divide numbers: function must return division of two numbers
#on input count system. 
#If count system went out of range, will be output of exception.
#If some number divided on zero, will be output of zerodivision exception
def test_div():
    assert divide_numbers('101010101','101010101',2) == '1'
    assert divide_numbers('5555','55',8) == '101'
    assert divide_numbers('500','10',10) == '50'
    assert divide_numbers('512','44',16) == '13'
    assert divide_numbers('10','2',2) == 'Number 10 or 2 isnt availabe in this count system!'
    assert divide_numbers('10','10',5010) == 'Base 5010 out of range!'
    assert divide_numbers('1','0',10) == 'You cant divide on Zero'
    assert divide_numbers('0','1',10) == '0'
   

#Case of finding remainder of division: function must return remainder from division of two numbers
#on input count system
#If count system went out of range, will be output of exception.
#If some number divided on zero, will be output of zerodivision exception
def test_rem():
    assert rem_numbers('1010010111','10101111',2) == '10001010'
    assert rem_numbers('777','77',8) == '7'
    assert rem_numbers('9521','55',10) == '6'
    assert rem_numbers('123','32',16) == '29'
    assert rem_numbers('4192','12',8) == 'Number 4192 or 12 isnt availabe in this count system!'
    assert rem_numbers('10','10',91295) == 'Base 91295 out of range!'
    assert rem_numbers('1','0',10) == 'You cant divide on Zero'
    assert rem_numbers('0','1',10) == '0'
    

if __name__ == "__main__":
    test_convert()
    out_green('\nAll convertation tests was passed!\n')
    test_sum()
    out_green("All sum tests was passed!\n")
    test_sub()
    print("All subtract tests was passed!\n")
    test_mul()
    print("All multiply tests was passed!\n")
    test_div()
    print("All division tests was passed!\n")
    test_rem()
    print("All remainding of division tests was passed!\n")

  

