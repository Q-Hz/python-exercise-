# 函数，打印衣服尺码和字样
def make_shirt(type,size='M'):
    """实参：衣服尺码,字样"""
    print("The type of the shirt is "+type.title())
    print("The size of the shirt is "+size)
make_shirt(type='T-shirt')

# 函数，打印衣服尺寸和字样
def make_shirt_(size,typeface='I love python'):
    """实参：尺码，字样"""
    print("The typeface of the shirt is: "+typeface.title())
    print("The siza of the shirt is "+size.title())
make_shirt_('L')
make_shirt_('m')

# 函数，指出城市对应的国家
def describe_city(city,county='China'):
    """实参：城市，国家"""
    print(city.title()+" is located in "+county)
describe_city('wuhan')
describe_city('London','England')
describe_city(county='USA',city='washington')