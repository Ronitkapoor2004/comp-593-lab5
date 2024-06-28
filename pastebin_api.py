'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/api/api_post.php'
API_DEV_KEY = '9vk2dIAWSDLczotzs_lwAsahJOk0OWxT'

def post_new_paste(title, body_text, expiration='N', listed=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group 
    post_parameters = {'api_dev_key':API_DEV_KEY, 'api_paste_private':'0', 'api_paste_expire_date': '1M', 'api_paste_name':title, 'api_paste_code': body_text, 'api_option':'paste'}
    resp_msg = requests.post(PASTEBIN_API_POST_URL,data=post_parameters)

    if resp_msg.status_code == requests.codes.ok:
        print(f'Posting new paste to Pastebin...success')
    else:
        print(f'Status code: { resp_msg.status_code } ({resp_msg.reason})')
        #print('Bad API request, invalid api_dev_key')
    return resp_msg.text