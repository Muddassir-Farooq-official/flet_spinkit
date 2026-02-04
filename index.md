# Introduction

FletSpinkit for Flet.

## Examples

```
import flet as ft

from flet_spinkit import FletSpinkit


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.Alignment.CENTER, bgcolor=ft.Colors.PURPLE_200, content=FletSpinkit(
                    tooltip="My new FletSpinkit Control tooltip",
                    value = "My new FletSpinkit Flet Control", 
                ),),

    )


ft.run(main)
```

## Classes

[FletSpinkit](FletSpinkit.md)


