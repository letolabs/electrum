from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string('''
<QRDialog@Popup>
    id: popup
    title: ''
    data: ''
    shaded: False
    AnchorLayout:
        anchor_x: 'center'
        BoxLayout:
            orientation: 'vertical'
            size_hint: 1, 1
            QRCodeWidget:
                id: qr
            TopLabel:
                text: root.data
            Widget:
                size_hint: 1, 0.2
            BoxLayout:
                size_hint: 1, None
                height: '48dp'
                Widget:
                    size_hint: 1, None
                    height: '48dp'
                Button:
                    size_hint: 1, None
                    height: '48dp'
                    text: _('Close')
                    on_release:
                        popup.dismiss()
''')

class QRDialog(Factory.Popup):
    def __init__(self, title, data):
        Factory.Popup.__init__(self)
        self.title = title
        self.data = data

    def on_open(self):
        self.ids.qr.set_data(self.data)