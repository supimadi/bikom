from crispy_forms.layout import (
    HTML, Div, Layout, Row, Field
)



STUDENT_REGIS_FORM_LAYOUT = Layout(
    Row(
        Div(Field('username', css_class='form-control form-control-sm'), css_class='col-12'),

        Div(Field('full_name', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('phone_number', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),

        Div(Field('photo', css_class='form-control form-control-sm'), css_class='col-12'),

        Div(Field('password1', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('password2', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),

        Div(HTML('<button class="py-2 mt-3 btn btn-block btn-danger">Daftarkan Saya!</button>'), css_class='col-12 d-grid'),

        # CSS class for the row form
        css_class="p-4",
    ),
)

STUDENT_PROFILE_FORM_LAYOUT = Layout(
    Row(
        Div(Field('instagram', css_class='form-control form-control-sm'), css_class='col-12'),
        Div(Field('chield_number', css_class='form-control form-control-sm'), css_class='col-12 col-md-4'),
        Div(Field('number_of_sibling', css_class='form-control form-control-sm'), css_class='col-12 col-md-4'),
        Div(Field('klass', css_class='form-control form-control-sm'), css_class='col-12 col-md-4'),
    )
)

BEST_FRIEND_FORM_LAYOUT = Layout(
    Row(
        Div(Field('full_name', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        Div(Field('phone_number', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
    )
)

APPOINTMENT_FORM_LAYOUT = Layout(
    Row(
        Div(Field('teacher', css_class='form-control form-control-sm'), css_class='col-12'),
        Div(Field('date', css_class='form-control form-control-sm'), css_class='col-12'),
        Div(Field('time', css_class='form-control form-control-sm'), css_class='col-12'),
        Div(Field('desc', css_class='form-control form-control-sm'), css_class='col-12'),
    )
)

def parent_form_layout(parent: str) -> Layout:
    layout = Layout(
        Row(
            Div(Field(f'{parent}_full_name', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
            Div(Field(f'{parent}_jobs', css_class='form-control form-control-sm'), css_class='col-12 col-md-6'),
        )
    )

    return layout

