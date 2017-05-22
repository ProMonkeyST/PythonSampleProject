book_info = ' The Three Musketeers: Alexandre Dumas'
formatted_book_info = book_info.strip().upper().replace(':', ' by')

print formatted_book_info

result_list = ['True', 'False', 'File not found']
result_string = ''.join(result_list)

print result_string

# def get_formatted_user_info(user):
# # Clear and concise. At a glance I can tell exactly what
# # the output should be. Note: this string could be returned
# # directly, but the string itself is too long to fit on the
# # page.
# output = 'Name: {user.name}, Age: {user.age}, Sex: {user.sex}'.format
# return output