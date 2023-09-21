# from django import forms
# from allauth.account.forms import LoginForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

# class CustomLoginForm(LoginForm):
#     def __init__(self, *args, **kwargs):
#         super(CustomLoginForm, self).__init__(*args, **kwargs)

#         # Add or override form fields with Tailwind CSS classes
#         self.fields['login'].widget.attrs.update({
#             'class': 'appearance-none border border-gray-300 rounded w-full py-2 px-3 mb-4 leading-tight focus:outline-none focus:border-blue-500'
#         })
#         self.fields['password'].widget.attrs.update({
#             'class': 'appearance-none border border-gray-300 rounded w-full py-2 px-3 mb-4 leading-tight focus:outline-none focus:border-blue-500'
#         })

#         # Crispy Forms configuration
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.form_class = 'space-y-4'
#         self.helper.add_input(Submit('submit', 'Login', css_class='bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded focus:outline-none focus:shadow-outline-blue active:bg-blue-700'))
#         self.helper.template_pack = 'tailwind'  # Specify the template pack
