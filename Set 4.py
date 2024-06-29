#!/usr/bin/env python
# coding: utf-8

# In[111]:


def bin_to_dec(binary_string):
    new_string = str(binary_string) 
    output = []

    for digit in new_string:
        output.append(int(digit))

    i = len(str(binary_string))
    a = 1
    Sum = 0

    while a <= i:
        for digit in output:
            New_Value = digit * (2 **(i-a))
            Sum += New_Value
            a += 1
        return Sum
            
bin_to_dec(10011)


# In[109]:


def dec_to_bin(number):

    new_list = []
    
    while True:
        remainder = number % 2
        quotient = number // 2
        number = quotient
        new_list.append(remainder)

        if quotient == 0:
            break

    new_list.reverse()
    new_string = ''.join(map(str, new_list))
    return new_string
  
dec_to_bin(19)


# In[5]:


def telephone_cipher(message):
    
    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }

    brand_new_list = []
    old_key = None
    
    for letter in message:
        if letter in encoder_dict:
            x = encoder_dict[letter]
            current_key = x[0]  
            
            if brand_new_list and old_key == current_key:
                brand_new_list.append('_')
            
            brand_new_list.append(x)
            old_key = current_key
    
    code = ''.join(brand_new_list)
    return code

telephone_cipher("I AM MIGS")


# In[239]:


def telephone_decipher(telephone_string):
    
    decipher_dict = {
        "0": " ",
        "2": "A",
        "22": "B",
        "222": "C",
        "3": "D",
        "33": "E",
        "333": "F",
        "4": "G",
        "44": "H",
        "444": "I",
        "5": "J",
        "55": "K",
        "555": "L",
        "6": "M",
        "66": "N",
        "666": "O",
        "7": "P",
        "77": "Q",
        "777": "R",
        "7777": "S",
        "8": "T",
        "88": "U",
        "888": "V",
        "9": "W",
        "99": "X",
        "999": "Y",
        "9999": "Z"
    }
    
    result = []
    current_digit = []

    for digit in telephone_string:
        if current_digit and digit != current_digit[-1]:
            result.append(decipher_dict.get("".join(current_digit), ""))
            current_digit = []
        current_digit.append(digit)
    
    if current_digit:
        result.append(decipher_dict.get("".join(current_digit), ""))
    
    return "".join(result)

telephone_decipher("44402606444_47777")


# In[ ]:




