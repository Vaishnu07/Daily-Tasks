import json
import requests
import datetime


# current_time = datetime.datetime.now()
#
# # Define start time and end time
# start_time = current_time - datetime.timedelta(hours=1)  # Example: 1 hour before current time
# end_time = current_time + datetime.timedelta(hours=1)
#
#
# # Convert timestamps to strings in desired format
# current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
# start_time_str = start_time.strftime("%Y-%m-%d %H:%M:%S")
# end_time_str = end_time.strftime("%Y-%m-%d %H:%M:%S")

headers = {
         "Content-Type": "application/json; charset=utf-8",
         "Cookie": "locale=en; _call_rpt_session=4874c8fa8e7fac0aed6344142b026cb5; _ga=GA1.2.2091385324.1715353767; _gid=GA1.2.30601427.1715353767; visitor_id=f7adee30-e03d-46a0-9af4-8f3bf4def6dd; cognito_user=true; amplify-redirected-from-hosted-ui=true; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.refreshToken=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.co9iugPwNc3IDWq-1Jftb_0oiKnbbBjYG4FPEuCdwsMllcRcXk6-wioJQb3ZI_Eu3SNa5g5Eud4NpdvpBoATMNSay5Fp15Z2LmfdrIyvEZphITDxhOGQJuguYVjgWkXV0kWeZoNTPqYndRlC3BsWp3YAPUt2xMPVtetvFfnLFl6-_2dxrnM693-L1H0YVhV_E3eIv6D72NQ2ncMjFqDzeSfxKR6XWFgNAJLa7UFhVMlvvPt1hW7RgfDTFeVnm3eE7_P9d-tJACqTCGZWTs8z6DOctyImQ6-le1vf6QnkKUrHhNDoVh-2eoAiutBnLEoId_MRBIsTSNcelVJ3_DRk4Q.DsTm-nzUPk1Et4B1.WcEdDIgcQliDSa6CMQbdb_ZBIj4q2kx0l4C6Rd7y08O-NPl1K5ctfCvmtu8SegPSDWlny3aY463fp9AAPlmd-rxt77YeYUIl-m3To0bvKImFa7cqKlzWaPylIKJ_oIMFW3p0DuF9Ib0jr-aN0CpIKxag876O7gZJ0HWbF3QnkIaMLzJSj82iUwJt2UCBnaeIBa2LEOgDCJ3vRjiELoTF2teuTXRYy8mLSOo0P0ir-7zDEwFIEC9kd_iSA3NELPyCtkowGioXciy5D360OiR9gn531ZLayH3YxN-kpfygFLMl8vjJ3xcK_1baaS0LqhPB2aHQSciwswEZqxp9M9HvZFJGykXBvbPm4sJeirTEGZUDhzOZ06UPIfBNE_s1KbaEVfxMRhAixbdpXQHJqg9CnXLXulIV2ixcKbX8-_H6XOcEAO6XKQnev-wpwV4QgfItS_4wLfSFM2ulkvINNOlSOqRMJXSyh5bWgk0C6KfRZwaDwX53EuvHRgwM36AVBieiXjqklK1pjbKXBTToSPGi5B8fHuZyU5ckyo05cvA71XQhdNzcLvE2DtV2Wzybpdj_CfzgkRDDkfGpYagFnH2zjB7joFB0692IkzYDOYtFAnEghlTZZV9Va8c23G7U9L0dA_dEmsZp0QjG3fXdhyIo3BpI9G7_lI-yX3raMpaCj3r7K7OqJTRAS1LLfO_pGzdmbpWxLZ4LNfMsQbdiCT6br2npjFdX99vHjGmZ8Yl9I9m0QI9ieyaBCWn50I70oJATM-WrR5o_YpUSObv6bcqxYx9fA8gohEDYAfp6TTrehTX2QIuTia9Q-9bHUDpzn9GlMeqgTO-YYSwg1oc3_cG0dzC8PDPgTYwxLelgjxwKeOg57itTCvoVHAB9LXSy0ZnRk9BNODgaNZqEHVP1gQs4eZvjQE-qS8uzyMmNTzj4jXSMkXsrBRz8vpvarwawFCjyiCVAIn-axFVXWMha48ZDHlV2mtlfNxRdpadDQpnI-D1ob2ShORi3Ts05LP1WrJnOUP5kTWys0UPW68kYuQxnUwaFSlrMwo-DWAKL7YlDHv-i7qeR4YybHKPQGWgGZDXpLnpY7MsI1Ns_7kETrcgI5dkBchEynfaCE9RbCWGswoJFYxSNQXdCjZBQMWBnMDCybVqIfIuulf1s-Q0SiR8B-zoGEvNZeB-QH8qtABB91Yr7aeVgiQPVm7bzfwbjdSSehAE1UXyZc0pqB_kJ24R-vcl5shubXCRksfbroMJaRj12XD6P7jm8g2pOAmpM7ZCYNmVyQZV40UnQov59F6lOThdoTYIH.We2YIGQBCM33B1kccQZ8hg; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.LastAuthUser=google_117702022248408890050; amplify-signin-with-hostedUI=true; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.userData={%22UserAttributes%22:[{%22Name%22:%22sub%22%2C%22Value%22:%228fc578b8-dee4-4ed1-877e-10403cdb6d1b%22}%2C{%22Name%22:%22identities%22%2C%22Value%22:%22[{%5C%22userId%5C%22:%5C%22117702022248408890050%5C%22%2C%5C%22providerName%5C%22:%5C%22Google%5C%22%2C%5C%22providerType%5C%22:%5C%22Google%5C%22%2C%5C%22issuer%5C%22:null%2C%5C%22primary%5C%22:true%2C%5C%22dateCreated%5C%22:1704461844206}]%22}%2C{%22Name%22:%22email_verified%22%2C%22Value%22:%22false%22}%2C{%22Name%22:%22phone_number_verified%22%2C%22Value%22:%22false%22}%2C{%22Name%22:%22email%22%2C%22Value%22:%22awsdev@libertyhomeguard.com%22}]%2C%22Username%22:%22google_117702022248408890050%22}; calltrk_user=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDYxNTg1ODcsInBsYW5zIjpbImNhbGxzIl0sImFjdGl2ZV9udW1iZXJzIjo0OTksImFjdGl2ZV9pbnRlZ3JhdGlvbnMiOlsiR29vZ2xlQWR3b3JkIiwiRmFjZWJvb2siLCJCaW5nIl0sImhhc19wY2kiOmZhbHNlfQ.7YmuFXE2qr3sVYEkX0canuudvYLCl0teEksLVNMmx40; account_id=704644062; account_name=Liberty%20Home%20Guard; has_ever_logged_in=1; _vwo_uuid_v2=DB7F4B9DA6A5EE7766D753B64FD556DB1|2ce773cebf0722afd016f32ffaaae409; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=DA4D02017FE5CFDF2A2848DCE6CAC8341; calltrk_state=active; calltrk_international=false; remember_device_token=fae243ed-0e0d-4896-a894-1f5d411d102d; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.clockDrift=0; last_visited_url=%2Fanalytics%2Fa%2F704644062%2Freports%2Fcall-list; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.idToken=eyJraWQiOiJ1VWFKbVBNMHUwT0lBK0ptd2dDcHlQN2NpTXY2cDd5d1h1cWFVUm1HYkFVPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiMkNwVDJGdThxTzYwSnphc2NrSE5yUSIsInN1YiI6IjhmYzU3OGI4LWRlZTQtNGVkMS04NzdlLTEwNDAzY2RiNmQxYiIsImNvZ25pdG86Z3JvdXBzIjpbInVzLWVhc3QtMV9IenBxQ2NFbllfR29vZ2xlIl0sImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfSHpwcUNjRW5ZIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjpmYWxzZSwiY29nbml0bzp1c2VybmFtZSI6Imdvb2dsZV8xMTc3MDIwMjIyNDg0MDg4OTAwNTAiLCJvcmlnaW5fanRpIjoiZmNjZGU5NGYtMjI0Ny00Y2I0LWI3MzgtZjM3MjBmN2Q3ZDU5IiwiYXVkIjoiNDV0bzcxaDRhaTc4bmQxajFyb2kyZWxjaGUiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMTc3MDIwMjIyNDg0MDg4OTAwNTAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNzA0NDYxODQ0MjA2In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTcxNTM1MzkxNiwiZXhwIjoxNzE1NjE5MjYzLCJpYXQiOjE3MTU1NTQ0NjQsImp0aSI6ImFkYjJhODA2LWFmOTMtNGZkMS1iMjFmLTU2NTA2YWU0MGMzYSIsImVtYWlsIjoiYXdzZGV2QGxpYmVydHlob21lZ3VhcmQuY29tIn0.o5wcKU0bkg-P3fJlyzOgm-mtHq9oiXq1zm6GQpnh0zhbxRT-ThXpMd8UsE-E84vtcOyMgbH7KFm1_P3zfxvC8AR0IODfMz84oz9votjHky5uLlCnn1ZP9ibA-UrVGXcfUPAkBox0rV6KIb3uFp0OScsvwItni9jKbTSAy_Gk558JZmtbPwVXFCY6rNlE0pyP4QZckjd7u8AvtM4UKEbL8NYYKRJz0F77tTqWYDb-KYGQl1vrjIEKQHMosIOkUlOLLZwjqcqYAbWocbfM0JFMQK0r1zUB5oot3blYbNDZXzbMyXyiL0zN7TfNDnCCp6E7TqtCopjHa401n25STo3hgg; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.accessToken=eyJraWQiOiJnRzBGOTgrcHhcL3o2dVJNbkszaUtwUlFTQnMwb1pyUDZvWFVZZTB1XC9XMkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4ZmM1NzhiOC1kZWU0LTRlZDEtODc3ZS0xMDQwM2NkYjZkMWIiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfSHpwcUNjRW5ZX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9IenBxQ2NFblkiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI0NXRvNzFoNGFpNzhuZDFqMXJvaTJlbGNoZSIsIm9yaWdpbl9qdGkiOiJmY2NkZTk0Zi0yMjQ3LTRjYjQtYjczOC1mMzcyMGY3ZDdkNTkiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIHBob25lIG9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNzE1MzUzOTE2LCJleHAiOjE3MTU1NTgwNjMsImlhdCI6MTcxNTU1NDQ2NCwianRpIjoiYzViNmY0YjQtZmIyYy00MDYxLWI0ZGQtZGI5MGFmMmY1MDAxIiwidXNlcm5hbWUiOiJnb29nbGVfMTE3NzAyMDIyMjQ4NDA4ODkwMDUwIn0.kCwAYtde_pHd_heUOXqmdfy_0fH5d-EjXPC0Arvbjq0pdB5Gu-ybmsn9La_toBXWPBJfRe3QY0ZLDLJicBp7E7ZycdfxF-Tvg87rBvGaZk901R2s-CRQlcHV-e4LjYiTR_g6BKpKphPcxn6ppKG9mAV9AsoY-QKbuKKMT3Cu_NNDdb5pKZXZcgelYBYzsRDfdxVh615OM5xV8ghQdsw4_zSyizI29TNF0PTbpByndFivsTZaDgxfy7U_aweF6eVroGqVtMJyZhPffV3S6lzDWu2YZErVDafNcFaxod30L2RGkYIZyhwDevu6LE6iossdrY8ztVRxforHBz6g9ZsAKw; fs_uid=#callrail.com#9d2eb180-43f5-4923-9702-0c8676b9505d:21153327-705b-4541-93a6-6139b14b6b4f:1715587139425::1#3b4bfcc3#/1746890224; fs_lua=1.1715587181487; _gat=1; _dd_s=rum=0&expire=1715588456611; CSRF-TOKEN=J9Pttt%2FVx60GaPRbGnY%2BfN6avBmTRpzg%2FB9w7qYbklztkx2u2oEIMhJsnHrRVZkQONf%2F65dteIwkXpRxQnX9AQ%3D%3D; last_request_at=1715587556; _vwo_sn=232973%3A2; _vwo_ds=3%3At_0%2Ca_0%3A0%241715354165%3A27.45085612%3A%3A11_0%2C9_0%3A26_0%2C25_0%3A1; _ga_HC10XK21E5=GS1.2.1715587531.9.1.1715587557.34.0.0"

}
payload = {"filters":{"for_company_sids":[748700824],"for_date_range":{"date_range":"custom","since":"2024-01-01","until":"2024-05-12"}},"config":{"interval":"total","selects":["tracker_details","source","start_time","duration","person_details","city_details","country_details","agent_details","device_type","keywords_details","referrer_domain","referrer_medium","landing_page_details","campaign","value","tag_details","qualified_details"],"metadata":[],"sort":"start_time","sort_direction":"desc"},"page":1,"per_page":None,"cursor_direction":None,"cursor":None,"type":"call-list"}
response = requests.put(url="https://app.callrail.com/a/704644062/reports/aggregations/fetch", data=json.dumps(payload),headers=headers)
# print(response.json())
calls_data=[]
total_page = 1288
for i in range(1,total_page):
     payload1={"filters":{"for_company_sids":[748700824],"for_date_range":{"date_range":"custom","since":"2024-01-01","until":"2024-05-12"}},"config":{"interval":"total","selects":["tracker_details","source","start_time","duration","person_details","city_details","country_details","agent_details","device_type","keywords_details","referrer_domain","referrer_medium","landing_page_details","campaign","value","tag_details","qualified_details"],"metadata":[],"sort":"start_time","sort_direction":"desc"},"page":i,"per_page":None,"cursor_direction":None,"cursor":None,"type":"call-list"}
     data_response = requests.put(url="https://app.callrail.com/a/704644062/reports/aggregations/fetch",
                                  data=json.dumps(payload1), headers=headers)
     data = data_response.json()
     print(data)
     for result in data["results"]:
         calls_data.append(result)
with open("2024data_Jan_May12.json", "w") as e:
    for durai in calls_data:
        json.dump(durai, e)
        e.write('\n')
# # Print the timestamps
# print("Current timestamp:", current_time_str)
# print("Start time:", start_time_str)
# print("End time:", end_time_str)