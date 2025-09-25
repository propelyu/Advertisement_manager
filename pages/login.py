from nicegui import ui, app, run
from components.header import show_header
import requests
from utils.api import base_url

_login_btn: ui.button = None


def _run_login(data):
    return requests.post(f"{base_url}/users/login", data=data)


async def _login_user(data):
    _login_btn.props(add="diasble loading")
    response = await run.cpu_bound(_run_login, data)
    _login_btn.props(remove="disable loading")
    if response.status_code == 200:
        json_data = response.json()
        app.storage.user["access_token"] = json_data["access_token"]
        ui.navigate.back()
    print(response.status_code, response.content)


@ui.page("/login")
def show_login_page():
    global _login_btn
    show_header()
    with ui.card().classes("w-96 p-6 space-y-4 mx-auto mt-20 "):
        ui.label("Log In").classes("text-2xl font-bold mb-4 text-center")

        email = ui.input("Email").props("type=email").classes("w-full")
        password = (
            ui.input(placeholder="password", password=True, password_toggle_button=True)
            .props("type=password")
            .classes("w-full")
        )

        _login_btn = (
            ui.button(
                "Log In",
                color="black",
                on_click=lambda: _login_user(
                    {"email": email.value, "password": password.value}
                ),
            )
            .props()
            .classes(
                "w-full bg-blue-600 text-white font-semibold py-2 rounded-lg hover:bg-blue-700"
            )
        )

        ui.label("Don't have an account?").classes("text-sm text-gray-600 text-center")
        ui.link("Sign up here", "/signup").classes(
            "text-sm text-black hover:underline text-center"
        )
