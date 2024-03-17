from numb3rs import validate



def format_only_accepts_4_numberblocks():
    ip = "1.2.3.4"
    ip = ip.split('.')
    #print(ip)
    assert len(validate(ip)) == 4


format_only_accepts_4_numberblocks()
