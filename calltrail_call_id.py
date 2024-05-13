import json
import requests


def fetch_call_ids():
    # Define headers with Content-Type and Authorization
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Token token=513f1278bb3f98dfee7a9817f860a09d"
    }

    # Send GET request to fetch data from the CallRail API
    # response = requests.get(url="https://api.callrail.com/v3/a/704644062/calls.json", headers=headers)
    # response_data = response.json()

    # Extract total pages from the response data
    #total_pages = response_data["total_pages"] + 1

    # Initialize an empty list to store call IDs
    call_ids = []

    # Iterate over each page of data
    for i in range(91, 100):
        print(f"Fetching page {i}...")

        # Send GET request for each page of data
        response = requests.get(url=f"https://api.callrail.com/v3/a/704644062/calls.json?page={i}", headers=headers)

        # Parse the response JSON
        response_data = response.json()
        print(response_data)

        # Append call IDs from each call to the call_ids list
        for call in response_data["calls"]:
            call_id = call.get("id")
            full_details = requests.get(url=f"https://api.callrail.com/v3/a/704644062/calls/{call_id}.json?fields=company_id,company_name,company_time_zone,created_at,device_type,first_call,formatted_call_type,formatted_business_phone_number,prior_calls,formatted_customer_name_or_phone_number,formatted_customer_phone_number,formatted_duration,formatted_tracking_phone_number,formatted_tracking_source,formatted_value,good_lead_call_id,good_lead_call_time,lead_status,note,source,source_name,tags,total_calls,value,waveforms,tracker_id,speaker_percent,keywords,medium,campaign,referring_url,landing_page_url,last_requested_url,referrer_domain,utm_source,utm_medium,utm_term,utm_content,utm_campaign,utma,utmb,utmc,utmv,utmz,ga,gclid,fbclid,msclkid,milestones,timeline_url,integration_data,keywords_spotted,call_highlights,call_summary,transcription,conversational_transcript,agent_email,keypad_entries", headers=headers)
            details= full_details.json()
            print(details)

            call_ids.append(details)
    print(call_ids)
    with open("data11.json", "w") as e:
        for dat in call_ids:
            json.dump(dat, e)
            e.write('\n')
    #         call_ids.append(details)
    # with open("datas.json", "w") as file:
    #     file.write(call_id)

    return details

if __name__ == "__main__":
    # Fetch call IDs
    call_ids = fetch_call_ids()

    # Print call IDs
    print("Call IDs:")
    for call_id in call_ids:
        print(call_id)












































# import json
# import requests
#
# headers = {
#          "Content-Type": "application/json; charset=utf-8",
#          "Cookie": "locale=en; _call_rpt_session=4874c8fa8e7fac0aed6344142b026cb5; _ga=GA1.2.2091385324.1715353767; _gid=GA1.2.30601427.1715353767; visitor_id=f7adee30-e03d-46a0-9af4-8f3bf4def6dd; cognito_user=true; amplify-redirected-from-hosted-ui=true; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.refreshToken=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.co9iugPwNc3IDWq-1Jftb_0oiKnbbBjYG4FPEuCdwsMllcRcXk6-wioJQb3ZI_Eu3SNa5g5Eud4NpdvpBoATMNSay5Fp15Z2LmfdrIyvEZphITDxhOGQJuguYVjgWkXV0kWeZoNTPqYndRlC3BsWp3YAPUt2xMPVtetvFfnLFl6-_2dxrnM693-L1H0YVhV_E3eIv6D72NQ2ncMjFqDzeSfxKR6XWFgNAJLa7UFhVMlvvPt1hW7RgfDTFeVnm3eE7_P9d-tJACqTCGZWTs8z6DOctyImQ6-le1vf6QnkKUrHhNDoVh-2eoAiutBnLEoId_MRBIsTSNcelVJ3_DRk4Q.DsTm-nzUPk1Et4B1.WcEdDIgcQliDSa6CMQbdb_ZBIj4q2kx0l4C6Rd7y08O-NPl1K5ctfCvmtu8SegPSDWlny3aY463fp9AAPlmd-rxt77YeYUIl-m3To0bvKImFa7cqKlzWaPylIKJ_oIMFW3p0DuF9Ib0jr-aN0CpIKxag876O7gZJ0HWbF3QnkIaMLzJSj82iUwJt2UCBnaeIBa2LEOgDCJ3vRjiELoTF2teuTXRYy8mLSOo0P0ir-7zDEwFIEC9kd_iSA3NELPyCtkowGioXciy5D360OiR9gn531ZLayH3YxN-kpfygFLMl8vjJ3xcK_1baaS0LqhPB2aHQSciwswEZqxp9M9HvZFJGykXBvbPm4sJeirTEGZUDhzOZ06UPIfBNE_s1KbaEVfxMRhAixbdpXQHJqg9CnXLXulIV2ixcKbX8-_H6XOcEAO6XKQnev-wpwV4QgfItS_4wLfSFM2ulkvINNOlSOqRMJXSyh5bWgk0C6KfRZwaDwX53EuvHRgwM36AVBieiXjqklK1pjbKXBTToSPGi5B8fHuZyU5ckyo05cvA71XQhdNzcLvE2DtV2Wzybpdj_CfzgkRDDkfGpYagFnH2zjB7joFB0692IkzYDOYtFAnEghlTZZV9Va8c23G7U9L0dA_dEmsZp0QjG3fXdhyIo3BpI9G7_lI-yX3raMpaCj3r7K7OqJTRAS1LLfO_pGzdmbpWxLZ4LNfMsQbdiCT6br2npjFdX99vHjGmZ8Yl9I9m0QI9ieyaBCWn50I70oJATM-WrR5o_YpUSObv6bcqxYx9fA8gohEDYAfp6TTrehTX2QIuTia9Q-9bHUDpzn9GlMeqgTO-YYSwg1oc3_cG0dzC8PDPgTYwxLelgjxwKeOg57itTCvoVHAB9LXSy0ZnRk9BNODgaNZqEHVP1gQs4eZvjQE-qS8uzyMmNTzj4jXSMkXsrBRz8vpvarwawFCjyiCVAIn-axFVXWMha48ZDHlV2mtlfNxRdpadDQpnI-D1ob2ShORi3Ts05LP1WrJnOUP5kTWys0UPW68kYuQxnUwaFSlrMwo-DWAKL7YlDHv-i7qeR4YybHKPQGWgGZDXpLnpY7MsI1Ns_7kETrcgI5dkBchEynfaCE9RbCWGswoJFYxSNQXdCjZBQMWBnMDCybVqIfIuulf1s-Q0SiR8B-zoGEvNZeB-QH8qtABB91Yr7aeVgiQPVm7bzfwbjdSSehAE1UXyZc0pqB_kJ24R-vcl5shubXCRksfbroMJaRj12XD6P7jm8g2pOAmpM7ZCYNmVyQZV40UnQov59F6lOThdoTYIH.We2YIGQBCM33B1kccQZ8hg; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.LastAuthUser=google_117702022248408890050; amplify-signin-with-hostedUI=true; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.userData={%22UserAttributes%22:[{%22Name%22:%22sub%22%2C%22Value%22:%228fc578b8-dee4-4ed1-877e-10403cdb6d1b%22}%2C{%22Name%22:%22identities%22%2C%22Value%22:%22[{%5C%22userId%5C%22:%5C%22117702022248408890050%5C%22%2C%5C%22providerName%5C%22:%5C%22Google%5C%22%2C%5C%22providerType%5C%22:%5C%22Google%5C%22%2C%5C%22issuer%5C%22:null%2C%5C%22primary%5C%22:true%2C%5C%22dateCreated%5C%22:1704461844206}]%22}%2C{%22Name%22:%22email_verified%22%2C%22Value%22:%22false%22}%2C{%22Name%22:%22phone_number_verified%22%2C%22Value%22:%22false%22}%2C{%22Name%22:%22email%22%2C%22Value%22:%22awsdev@libertyhomeguard.com%22}]%2C%22Username%22:%22google_117702022248408890050%22}; calltrk_user=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDYxNTg1ODcsInBsYW5zIjpbImNhbGxzIl0sImFjdGl2ZV9udW1iZXJzIjo0OTksImFjdGl2ZV9pbnRlZ3JhdGlvbnMiOlsiR29vZ2xlQWR3b3JkIiwiRmFjZWJvb2siLCJCaW5nIl0sImhhc19wY2kiOmZhbHNlfQ.7YmuFXE2qr3sVYEkX0canuudvYLCl0teEksLVNMmx40; account_id=704644062; account_name=Liberty%20Home%20Guard; has_ever_logged_in=1; _vwo_uuid_v2=DB7F4B9DA6A5EE7766D753B64FD556DB1|2ce773cebf0722afd016f32ffaaae409; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=DA4D02017FE5CFDF2A2848DCE6CAC8341; calltrk_state=active; calltrk_international=false; remember_device_token=fae243ed-0e0d-4896-a894-1f5d411d102d; last_visited_url=%2Fanalytics%2Fa%2F704644062%2Freports%2Fcall-list; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.idToken=eyJraWQiOiJ1VWFKbVBNMHUwT0lBK0ptd2dDcHlQN2NpTXY2cDd5d1h1cWFVUm1HYkFVPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoieVhZSy1WMTlPZmZWSmphSVhJNkRKZyIsInN1YiI6IjhmYzU3OGI4LWRlZTQtNGVkMS04NzdlLTEwNDAzY2RiNmQxYiIsImNvZ25pdG86Z3JvdXBzIjpbInVzLWVhc3QtMV9IenBxQ2NFbllfR29vZ2xlIl0sImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfSHpwcUNjRW5ZIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjpmYWxzZSwiY29nbml0bzp1c2VybmFtZSI6Imdvb2dsZV8xMTc3MDIwMjIyNDg0MDg4OTAwNTAiLCJvcmlnaW5fanRpIjoiZmNjZGU5NGYtMjI0Ny00Y2I0LWI3MzgtZjM3MjBmN2Q3ZDU5IiwiYXVkIjoiNDV0bzcxaDRhaTc4bmQxajFyb2kyZWxjaGUiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMTc3MDIwMjIyNDg0MDg4OTAwNTAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNzA0NDYxODQ0MjA2In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTcxNTM1MzkxNiwiZXhwIjoxNzE1NDk1MjU2LCJpYXQiOjE3MTU0MzA0NTYsImp0aSI6ImJkNGFlMDk4LTU0Y2ItNDkxYi04ZDliLWRiYTdhMjEwZWU2MiIsImVtYWlsIjoiYXdzZGV2QGxpYmVydHlob21lZ3VhcmQuY29tIn0.eFkltdbqpJLRq8iHya0PxyHF0cibMBp-loVO7S0Vri6FSOojf9xbXK8Lrj3FIcktN7N-K4EpFPDrdPWcg65ZUF85lokbhPAzkmQUVgc00CLOg1PfPMlJYfXmf4j9D_KojAg1-Dk1fWjauykcZUy6EaBE6ReGMS3o7LbhyRFNshDmYN-uf63NCVTzN0GU-gln_4PLoMSrRzdoYElLtE3PAzV1m_B6c6LBp_khuPtk1Zho1PjUOEx9Ir_WrjdcXtgufOyM1oAVs8KI34yefFdhcRpIU3ybzy_MtX3fAPAPuVVYDDb0YOxICTww2QMqJnYlFsgi0i-T7PfkCWSMOnEmFw; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.accessToken=eyJraWQiOiJnRzBGOTgrcHhcL3o2dVJNbkszaUtwUlFTQnMwb1pyUDZvWFVZZTB1XC9XMkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4ZmM1NzhiOC1kZWU0LTRlZDEtODc3ZS0xMDQwM2NkYjZkMWIiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfSHpwcUNjRW5ZX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9IenBxQ2NFblkiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI0NXRvNzFoNGFpNzhuZDFqMXJvaTJlbGNoZSIsIm9yaWdpbl9qdGkiOiJmY2NkZTk0Zi0yMjQ3LTRjYjQtYjczOC1mMzcyMGY3ZDdkNTkiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIHBob25lIG9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNzE1MzUzOTE2LCJleHAiOjE3MTU0MzQwNTYsImlhdCI6MTcxNTQzMDQ1NiwianRpIjoiMjQ0YjU4ODEtMzM0Ny00N2ZlLWI1MGQtYWU2NDMwOGEwY2ZiIiwidXNlcm5hbWUiOiJnb29nbGVfMTE3NzAyMDIyMjQ4NDA4ODkwMDUwIn0.VS2Znp2QpyRVvCjLd2cYSpaXtFNYFWu7kM_ZtmNYOogOyN_P7BhlLUbBQnLyV7AxtdwxGgvFeeqr-YMpUFF_B1SjcxOGCWlwmWlISDvVtTLQAj15BiLQTzmJTeHQvtj_B3zZaQ-SGO9ENdJXXbCSX49UkcTfzl0yzzFmDW4ZoS7mFJvA8vvAszWMjTnCv75zN-m6rahDSQh5lYplIy36MXf877FrFXS24bRx5XODgYP4zQ4xQ-1uThQxZK5RjyRGnaUGjBSY29hUugPw2TVe0MhJje0l7xSryx5QUKcEXmzL-rppn-dwChsgubgJBj8mriQ7DwOsOU50rcurZRYFxQ; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.clockDrift=0; fs_lua=1.1715483201896; fs_uid=#callrail.com#9d2eb180-43f5-4923-9702-0c8676b9505d:52cba4f9-e71b-4911-b0ce-9db98fe4fdf2:1715483201896::1#3b4bfcc3#/1746890207; _dd_s=rum=0&expire=1715484172936; _gat=1; CSRF-TOKEN=1ssWimP4x4BMTg6Kh3hrguxypy9GK0aI%2Fbe7SoVh7m4ci%2BaSZqwIH1hKZqtMW8zuCj%2Fk3UIAouQl9l%2FVYQ%2BBMw%3D%3D; last_request_at=1715483274; _vwo_sn=129034%3A1; _vwo_ds=3%3At_0%2Ca_0%3A0%241715354165%3A27.45085612%3A%3A11_0%2C9_0%3A26_0%2C25_0%3A1; _ga_HC10XK21E5=GS1.2.1715483272.6.1.1715483274.58.0.0"
#      }
# payload = {"filters":{"for_company_sids":[748700824],"for_date_range":{"date_range":"custom","since":"2023-07-01","until":"2023-12-31"}},"config":{"interval":"total","selects":["tracker_details","source","start_time","duration","person_details","city_details","country_details","agent_details","device_type","keywords_details","referrer_domain","referrer_medium","landing_page_details","campaign","value","tag_details","qualified_details"],"metadata":[],"sort":"start_time","sort_direction":"desc"},"page":1,"per_page":None,"cursor_direction":None,"cursor":None,"type":"call-list"}
# response = requests.put(url="https://app.callrail.com/a/704644062/reports/aggregations/fetch", data=json.dumps(payload),headers=headers)
# #print(response.json())
# calls_data=[]
# total_page = 1310
# for i in range(1,total_page):
#      payload1={"filters":{"for_company_sids":[748700824],"for_date_range":{"date_range":"custom","since":"2023-07-01","until":"2023-12-31"}},"config":{"interval":"total","selects":["tracker_details","source","start_time","duration","person_details","city_details","country_details","agent_details","device_type","keywords_details","referrer_domain","referrer_medium","landing_page_details","campaign","value","tag_details","qualified_details"],"metadata":[],"sort":"start_time","sort_direction":"desc"},"page":i,"per_page":None,"cursor_direction":None,"cursor":None,"type":"call-list"}
#      data_response = requests.put(url="https://app.callrail.com/a/704644062/reports/aggregations/fetch",
#                              data=json.dumps(payload1), headers=headers)
#      data = data_response.json()
#      print(data)
#      for result in data["results"]:
#          calls_data.append(result)
# with open("2023data_July_Dec.json", "w") as e:
#     for durai in calls_data:
#         json.dump(durai, e)
#         e.write('\n')


# import json
# import requests
#
# headers = {
#          "Content-Type": "application/json; charset=utf-8",
#          "Cookie": "locale=en; _call_rpt_session=4874c8fa8e7fac0aed6344142b026cb5; _ga=GA1.2.2091385324.1715353767; _gid=GA1.2.30601427.1715353767; visitor_id=f7adee30-e03d-46a0-9af4-8f3bf4def6dd; cognito_user=true; amplify-redirected-from-hosted-ui=true; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.refreshToken=eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.co9iugPwNc3IDWq-1Jftb_0oiKnbbBjYG4FPEuCdwsMllcRcXk6-wioJQb3ZI_Eu3SNa5g5Eud4NpdvpBoATMNSay5Fp15Z2LmfdrIyvEZphITDxhOGQJuguYVjgWkXV0kWeZoNTPqYndRlC3BsWp3YAPUt2xMPVtetvFfnLFl6-_2dxrnM693-L1H0YVhV_E3eIv6D72NQ2ncMjFqDzeSfxKR6XWFgNAJLa7UFhVMlvvPt1hW7RgfDTFeVnm3eE7_P9d-tJACqTCGZWTs8z6DOctyImQ6-le1vf6QnkKUrHhNDoVh-2eoAiutBnLEoId_MRBIsTSNcelVJ3_DRk4Q.DsTm-nzUPk1Et4B1.WcEdDIgcQliDSa6CMQbdb_ZBIj4q2kx0l4C6Rd7y08O-NPl1K5ctfCvmtu8SegPSDWlny3aY463fp9AAPlmd-rxt77YeYUIl-m3To0bvKImFa7cqKlzWaPylIKJ_oIMFW3p0DuF9Ib0jr-aN0CpIKxag876O7gZJ0HWbF3QnkIaMLzJSj82iUwJt2UCBnaeIBa2LEOgDCJ3vRjiELoTF2teuTXRYy8mLSOo0P0ir-7zDEwFIEC9kd_iSA3NELPyCtkowGioXciy5D360OiR9gn531ZLayH3YxN-kpfygFLMl8vjJ3xcK_1baaS0LqhPB2aHQSciwswEZqxp9M9HvZFJGykXBvbPm4sJeirTEGZUDhzOZ06UPIfBNE_s1KbaEVfxMRhAixbdpXQHJqg9CnXLXulIV2ixcKbX8-_H6XOcEAO6XKQnev-wpwV4QgfItS_4wLfSFM2ulkvINNOlSOqRMJXSyh5bWgk0C6KfRZwaDwX53EuvHRgwM36AVBieiXjqklK1pjbKXBTToSPGi5B8fHuZyU5ckyo05cvA71XQhdNzcLvE2DtV2Wzybpdj_CfzgkRDDkfGpYagFnH2zjB7joFB0692IkzYDOYtFAnEghlTZZV9Va8c23G7U9L0dA_dEmsZp0QjG3fXdhyIo3BpI9G7_lI-yX3raMpaCj3r7K7OqJTRAS1LLfO_pGzdmbpWxLZ4LNfMsQbdiCT6br2npjFdX99vHjGmZ8Yl9I9m0QI9ieyaBCWn50I70oJATM-WrR5o_YpUSObv6bcqxYx9fA8gohEDYAfp6TTrehTX2QIuTia9Q-9bHUDpzn9GlMeqgTO-YYSwg1oc3_cG0dzC8PDPgTYwxLelgjxwKeOg57itTCvoVHAB9LXSy0ZnRk9BNODgaNZqEHVP1gQs4eZvjQE-qS8uzyMmNTzj4jXSMkXsrBRz8vpvarwawFCjyiCVAIn-axFVXWMha48ZDHlV2mtlfNxRdpadDQpnI-D1ob2ShORi3Ts05LP1WrJnOUP5kTWys0UPW68kYuQxnUwaFSlrMwo-DWAKL7YlDHv-i7qeR4YybHKPQGWgGZDXpLnpY7MsI1Ns_7kETrcgI5dkBchEynfaCE9RbCWGswoJFYxSNQXdCjZBQMWBnMDCybVqIfIuulf1s-Q0SiR8B-zoGEvNZeB-QH8qtABB91Yr7aeVgiQPVm7bzfwbjdSSehAE1UXyZc0pqB_kJ24R-vcl5shubXCRksfbroMJaRj12XD6P7jm8g2pOAmpM7ZCYNmVyQZV40UnQov59F6lOThdoTYIH.We2YIGQBCM33B1kccQZ8hg; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.LastAuthUser=google_117702022248408890050; amplify-signin-with-hostedUI=true; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.userData={%22UserAttributes%22:[{%22Name%22:%22sub%22%2C%22Value%22:%228fc578b8-dee4-4ed1-877e-10403cdb6d1b%22}%2C{%22Name%22:%22identities%22%2C%22Value%22:%22[{%5C%22userId%5C%22:%5C%22117702022248408890050%5C%22%2C%5C%22providerName%5C%22:%5C%22Google%5C%22%2C%5C%22providerType%5C%22:%5C%22Google%5C%22%2C%5C%22issuer%5C%22:null%2C%5C%22primary%5C%22:true%2C%5C%22dateCreated%5C%22:1704461844206}]%22}%2C{%22Name%22:%22email_verified%22%2C%22Value%22:%22false%22}%2C{%22Name%22:%22phone_number_verified%22%2C%22Value%22:%22false%22}%2C{%22Name%22:%22email%22%2C%22Value%22:%22awsdev@libertyhomeguard.com%22}]%2C%22Username%22:%22google_117702022248408890050%22}; calltrk_user=eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDYxNTg1ODcsInBsYW5zIjpbImNhbGxzIl0sImFjdGl2ZV9udW1iZXJzIjo0OTksImFjdGl2ZV9pbnRlZ3JhdGlvbnMiOlsiR29vZ2xlQWR3b3JkIiwiRmFjZWJvb2siLCJCaW5nIl0sImhhc19wY2kiOmZhbHNlfQ.7YmuFXE2qr3sVYEkX0canuudvYLCl0teEksLVNMmx40; account_id=704644062; account_name=Liberty%20Home%20Guard; has_ever_logged_in=1; _vwo_uuid_v2=DB7F4B9DA6A5EE7766D753B64FD556DB1|2ce773cebf0722afd016f32ffaaae409; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=DA4D02017FE5CFDF2A2848DCE6CAC8341; calltrk_state=active; calltrk_international=false; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.idToken=eyJraWQiOiJ1VWFKbVBNMHUwT0lBK0ptd2dDcHlQN2NpTXY2cDd5d1h1cWFVUm1HYkFVPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiR0ZHV3ZUeENia2NFZk13N2dNc3kwZyIsInN1YiI6IjhmYzU3OGI4LWRlZTQtNGVkMS04NzdlLTEwNDAzY2RiNmQxYiIsImNvZ25pdG86Z3JvdXBzIjpbInVzLWVhc3QtMV9IenBxQ2NFbllfR29vZ2xlIl0sImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tXC91cy1lYXN0LTFfSHpwcUNjRW5ZIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjpmYWxzZSwiY29nbml0bzp1c2VybmFtZSI6Imdvb2dsZV8xMTc3MDIwMjIyNDg0MDg4OTAwNTAiLCJvcmlnaW5fanRpIjoiZmNjZGU5NGYtMjI0Ny00Y2I0LWI3MzgtZjM3MjBmN2Q3ZDU5IiwiYXVkIjoiNDV0bzcxaDRhaTc4bmQxajFyb2kyZWxjaGUiLCJpZGVudGl0aWVzIjpbeyJ1c2VySWQiOiIxMTc3MDIwMjIyNDg0MDg4OTAwNTAiLCJwcm92aWRlck5hbWUiOiJHb29nbGUiLCJwcm92aWRlclR5cGUiOiJHb29nbGUiLCJpc3N1ZXIiOm51bGwsInByaW1hcnkiOiJ0cnVlIiwiZGF0ZUNyZWF0ZWQiOiIxNzA0NDYxODQ0MjA2In1dLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTcxNTM1MzkxNiwiZXhwIjoxNzE1NDI5NTQ4LCJpYXQiOjE3MTUzNjQ3NDgsImp0aSI6IjQ4ZTQ5NGI2LTg5ZjItNDY4ZS1hMmZiLTFhODE5OTM3MWJiZSIsImVtYWlsIjoiYXdzZGV2QGxpYmVydHlob21lZ3VhcmQuY29tIn0.dZhCj5ow7cw0Ltx-xcend4QVOmQUiarLF4j6oEX-VDTwIVibRNVwzIA88sInmMHdICvRMKuT94iwnsqNhIrgBmPwjRiXtxKOkm_83ekCU2V_kKcr87kVu5uzPO_ImpUquU6uLaQt4QcrUiXrXsX1QGaBf8vRHPMGjwnD4gDALbIvq3bvD6NSn2Kem5EhXqOc2rvXsGhoyGqawHS3fwbMOWmm5JcLMZ-YZjszQo5qs2u6FAGKh88b0T3JeTZxpzB3J9cMjT-ELJ3VvutAVUoU_-77Rf5PP6kpcTVZZS_ABVGnJrG_CVP7Abm32abVKnsnrZdWT9fXXPzzxXgXoZk77w; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.accessToken=eyJraWQiOiJnRzBGOTgrcHhcL3o2dVJNbkszaUtwUlFTQnMwb1pyUDZvWFVZZTB1XC9XMkE9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiI4ZmM1NzhiOC1kZWU0LTRlZDEtODc3ZS0xMDQwM2NkYjZkMWIiLCJjb2duaXRvOmdyb3VwcyI6WyJ1cy1lYXN0LTFfSHpwcUNjRW5ZX0dvb2dsZSJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9IenBxQ2NFblkiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI0NXRvNzFoNGFpNzhuZDFqMXJvaTJlbGNoZSIsIm9yaWdpbl9qdGkiOiJmY2NkZTk0Zi0yMjQ3LTRjYjQtYjczOC1mMzcyMGY3ZDdkNTkiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIHBob25lIG9wZW5pZCBwcm9maWxlIGVtYWlsIiwiYXV0aF90aW1lIjoxNzE1MzUzOTE2LCJleHAiOjE3MTUzNjgzNDgsImlhdCI6MTcxNTM2NDc0OCwianRpIjoiMWJjNjFlYjYtYzc3Yy00YWFkLTk4OTYtODFjN2NiMGQ3NzZlIiwidXNlcm5hbWUiOiJnb29nbGVfMTE3NzAyMDIyMjQ4NDA4ODkwMDUwIn0.IJ_5PlS6-jVBco818DEH7pW07jQzRtipGoqWnILpg5XMAw_8BDBceiw3c89t7DvngJcEq8GpzjMo-U_A4A8NifCdzi5uonrxejX1FQQSPGtmjsPUoR15s44xxkX0elp23iaaV-mmIu0vWzc1axpKgOSS7jZEo_Fk8Hz2GSu3WOqs8nXgdEGtDl9h5j8il_lcJi8--TGFRS27uaEd7ZixkMSCoPcSJjLx9FJN-Q_bq1Ir4-ExP3gb-bLWCF8mSaX4zpP56LGe3j9jNrWBz13aqhC4NG8z_QV01CjYzSY_amaD4LDzl339c1um8kzicTl5ZFIwO6jWmZfejnC7aHlNUw; CognitoIdentityServiceProvider.45to71h4ai78nd1j1roi2elche.google_117702022248408890050.clockDrift=1; _ga_HC10XK21E5=GS1.2.1715362217.3.1.1715364792.11.0.0; remember_device_token=fae243ed-0e0d-4896-a894-1f5d411d102d; last_visited_url=%2Fanalytics%2Fa%2F704644062%2Freports%2Fcall-list; fs_lua=1.1715428525452; fs_uid=#callrail.com#9d2eb180-43f5-4923-9702-0c8676b9505d:19fb5358-e734-4f64-8719-bc4dad43d27f:1715428525452::1#3b4bfcc3#/1746890198; _dd_s=rum=0&expire=1715429680021; last_request_at=1715428780; _vwo_sn=74354%3A3; _vwo_ds=3%3At_0%2Ca_0%3A0%241715354165%3A27.45085612%3A%3A11_0%2C9_0%3A26_0%2C25_0%3A1; CSRF-TOKEN=0inHzSj1imMS8Jq2Hl2SPQ%2BvjTtNWs2TJslLVjBb3H0YaTfVLaFF%2FAb08pfVfjVR6eLOyUlxKf%2F%2BiK%2FJ1DWzIA%3D%3D"
#      }
# payload = {"filters":{"for_company_sids":[748700824],"for_date_range":{"date_range":"custom","since":"2023-01-01","until":"2023-03-31"}},"config":{"interval":"total","selects":["tracker_details","source","start_time","duration","person_details","city_details","country_details","agent_details","device_type","keywords_details","referrer_domain","referrer_medium","landing_page_details","campaign","value","tag_details","qualified_details"],"metadata":[],"sort":"start_time","sort_direction":"desc"},"page":1,"per_page":None,"cursor_direction":None,"cursor":None,"type":"call-list"}
# response = requests.put(url="https://app.callrail.com/a/704644062/reports/aggregations/fetch", data=json.dumps(payload),headers=headers)
# print(response.json())
# calls_data=[]
# total_page = 428
# for i in range(1,total_page):
#      payload1={"filters":{"for_company_sids":[748700824],"for_date_range":{"date_range":"last_year","since":None,"until":None}},"config":{"interval":"total","selects":["tracker_details","source","start_time","duration","person_details","city_details","country_details","agent_details","device_type","keywords_details","referrer_domain","referrer_medium","landing_page_details","campaign","value","tag_details","qualified_details"],"metadata":[],"sort":"start_time","sort_direction":"desc"},"page":i,"per_page":None,"cursor_direction":None,"cursor":None,"type":"call-list"}
#      data_response = requests.put(url="https://app.callrail.com/a/704644062/reports/aggregations/fetch",
#                              data=json.dumps(payload1), headers=headers)
#      data = data_response.json()
#      print(data)
#      for result in data["results"]:
#          calls_data.append(result)
# with open("2023JAN_MARCH_.json", "w") as e:
#     for durai in calls_data:
#         json.dump(durai, e)
#         e.write('\n')