from nicegui import ui, run
from components.header import show_header
import requests
from utils.api import base_url

_signup_btn: ui.button = None


def _run_signup(data):
    return requests.post(f"{base_url}/users/register", data=data)


async def _signup(data):
    _signup_btn.props(add="disable loading")
    response = await run.cpu_bound(_run_signup, data)
    print(response.status_code, response.content)
    _signup_btn.props(remove="disable loading")
    if response.status_code == 200:
        return ui.navigate.to("/login")
    elif response.status_code == 409:
        return ui.notify(message="User Already Exist", type="warning")


@ui.page("/signup")
def show_signup_page():
    show_header()
    with ui.column().classes(
        "min-h-screen w-full items-center bg-gray-100   justify-center p-0 bg-cover rounded-lg"
    ):
        with ui.column().classes("w-full max-w-xl p-8 shadow-lg rounded-xl"):
            ui.label("Sign Up").classes(
                "text-2xl font-bold mb-6 flex flex-row justify-center items-center"
            )

            # Select button (dropdown)
            register = ui.radio(["Guest", "Vendor"], value="Guest").classes(
                "w-full flex flex-row items-center justify-center "
            )

            form_container = ui.column().classes("space-y-4 w-full bg-gray-100")
            ui.label("Already have an account?").classes(
                "text-sm text-gray-600 text-center"
            )
            ui.link("Log in here", "/login").classes(
                "text-sm text-black font-bold hover:underline text-center"
            )

            def render_form():
                global _signup_btn
                form_container.clear()
                if register.value == "Guest":
                    with form_container:
                        full_name = ui.input("Full Name").classes("w-full")
                        email = ui.input("Email").props("type=email").classes("w-full")
                        password = (
                            ui.input(
                                placeholder="Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password")
                            .classes("w-full")
                        )
                        confirm_password = (
                            ui.input(
                                placeholder="Confirm Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password")
                            .classes("w-full")
                        )
                        _signup_btn = ui.button(
                            "Sign Up",
                            color="black",
                            on_click=lambda: _signup(
                                {
                                    "full_name": full_name.value,
                                    "email": email.value,
                                    "password": password.value,
                                    "confirm_password": confirm_password.value,
                                    "role": "Guest",
                                }
                            ),
                        ).classes("w-full text-white")
                else:
                    with form_container:
                        full_name = ui.input(placeholder="Full Name").classes("w-full")
                        email = (
                            ui.input(placeholder="Email")
                            .props("type=email")
                            .classes("w-full")
                        )
                        password = (
                            ui.input(
                                placeholder="Password",
                                password=True,
                                password_toggle_button=True,
                            )
                            .props("type=password")
                            .classes("w-full")
                        )
                        confirm_password = ui.input(
                            placeholder="Confirm Password",
                            password=True,
                            password_toggle_button=True,
                        ).classes("w-full")

                        _signup_btn = ui.button(
                            "Sign Up",
                            on_click=lambda: _signup(
                                {
                                    "full_name": full_name.value,
                                    "email": email.value,
                                    "password": password.value,
                                    "confirm_password": confirm_password.value,
                                    "role": "Vendor",
                                }
                            ),
                        ).classes("w-full")

            render_form()

            register.on_value_change(lambda e: render_form())
