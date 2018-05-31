def normalized_phone(phone):
    if( (len(phone) > 2) and (phone != "(null)") ):
        # remove symbol
        phone = phone.replace("+","").replace("*","").replace(" ", "").replace("?", "").replace("(", "").replace(")", "").replace(".", "").replace("/", "").replace("-", "")

        phone = list(phone)

        # replace first 0 with 62
        if(int(phone[0])==0):
            phone.pop(0)
            phone.insert(0, "62")

        phone = ''.join(phone)
        #
        if(str(phone[:3])=="620"):
            phone = list(phone)
            phone.pop(2)

        phone = ''.join(phone)

    return str(phone)

test_case = [
    { "phone" : "-", "normalized_phone" : "-" },
    { "phone" : "0", "normalized_phone" : "0" },
    { "phone" : "62", "normalized_phone" : "62" },
    { "phone" : "(null)", "normalized_phone" : "(null)" },
    { "phone" : "+6281298490805", "normalized_phone" : "6281298490805" },
    { "phone" : "6281298490805", "normalized_phone" : "6281298490805" },
    { "phone" : "08119284411", "normalized_phone" : "628119284411" },
    { "phone" : "+1 (804) 244-3470", "normalized_phone" : "18042443470" },
    { "phone" : "*083831397998", "normalized_phone" : "6283831397998" },
    { "phone" : "+1408-888-4919", "normalized_phone" : "14088884919" },
    { "phone" : "+1 917 856 9984", "normalized_phone" : "19178569984" },
    { "phone" : "?+62 822 42973752?", "normalized_phone" : "6282242973752" },
    { "phone" : "646.490.2691", "normalized_phone" : "6464902691" },
    { "phone" : "+626281322522898", "normalized_phone" : "626281322522898" },
    { "phone" : "+85 2-92730944", "normalized_phone" : "85292730944" },
    { "phone" : "+62-081377229637", "normalized_phone" : "6281377229637" },
    { "phone" : "82664848155", "normalized_phone" : "82664848155" },
    { "phone" : "08111338062 / 08788", "normalized_phone" : "62811133806208788" },
    { "phone" : "(021) 5736789", "normalized_phone" : "62215736789" }
]

for i, val in enumerate(test_case):
    phone = val["phone"]
    normal = val["normalized_phone"]

    print(normalized_phone(phone) + " => " + str(normalized_phone(phone)==normal))

    