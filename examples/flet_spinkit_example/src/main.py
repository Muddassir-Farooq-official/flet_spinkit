import flet as ft
from flet_spinkit import FletSpinkit

def main(page: ft.Page):
    page.title = "Flet Spinkit Gallery"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    # Get all animation names from our Spinkits class
    # We filter out internal Python attributes (starting with __)
    spinkit_types = [
        value for name, value in FletSpinkit.Spinkits.__dict__.items() 
        if not name.startswith("__") and isinstance(value, str)
    ]

    gallery = ft.ResponsiveRow(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    for sk_type in spinkit_types:
        gallery.controls.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        FletSpinkit(
                            type=sk_type,
                            color=ft.Colors.BLACK,
                            size=50
                        ),
                        ft.Text(sk_type, size=12, weight=ft.FontWeight.W_300)
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                padding=10,
                col={"sm": 6, "md": 4, "lg": 2}, # Responsive layout
                bgcolor=ft.Colors.AMBER,
            )
        )

    page.add(
        ft.Text("Flet Spinkit Full Showcase", size=32, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        gallery
    )

ft.run(main)