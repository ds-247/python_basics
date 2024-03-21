import requests

def  get_name(name) :
    fullname = name['title'] + ' ' + name['first'] + ' ' + name['last'];
    # return name['title'], name['first'], name['last'];
    return fullname;

def get_status(json):
    print(json['statusCode'])

def get_location(location) :
   street =  "Street - " +str( location['street']['number']) + "  " + location['street']['name'];
   city = 'City - ' + location['city']
   state = "State - " + location ['state'];
   return street + city + state;

def get_dob(dob):
    return dob['date'] + ' ' + str(dob['age']);

def  get_registered_data(json) :
    pass;


def  main() :
    resp = requests.get('https://api.freeapi.app/api/v1/public/randomusers/user/random');
    resp = resp.json();
    data = resp['data'];

    # print(data)

    get_status(resp);
    name = get_name(data['name']);
    dob  = get_dob(data['dob']);
    location = get_location(data['location']);
    email = data['email'];
    phone = data['phone'];

    print(f"The api belongs to {name} whose dob is {dob} is located at {location} , having an email  {email}, along with the phone number {phone} ")


if __name__  == '__main__' :
    main();



# status = resp.status_code;
# print("Status of request ", status)

# headers = resp.headers;
# print('Header responses : ', headers);

# encoding = resp.encoding;
# print(encoding)

# text = resp.text;



# print(text)
# print(resp.json())