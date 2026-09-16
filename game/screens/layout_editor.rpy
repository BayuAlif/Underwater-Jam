default layout_editor_target = "mc"
default layout_editor_x = 0.25
default layout_editor_y = 0.85
default layout_editor_zoom = 0.70


init python:

    layout_editor_data = {
        "mc": {
            "image": "mc default",
            "crop": (0, 590, 500, 490),
            "x": 0.25,
            "y": 0.85,
            "zoom": 0.70
        },

        "cory": {
            "image": "cory talk",
            "crop": None,
            "x": 0.65,
            "y": 0.85,
            "zoom": 0.50
        },

        "bass": {
            "image": "bass default",
            "crop": None,
            "x": 0.75,
            "y": 0.85,
            "zoom": 0.50
        },

        "uceng": {
            "image": "uceng default",
            "crop": None,
            "x": 0.75,
            "y": 0.85,
            "zoom": 0.60
        },

        "lele": {
            "image": "lele default",
            "crop": None,
            "x": 0.75,
            "y": 0.85,
            "zoom": 0.50
        },

        "gator": {
            "image": "gator default",
            "crop": None,
            "x": 0.75,
            "y": 0.85,
            "zoom": 0.50
        }
    }


    def layout_editor_select(target):

        data = layout_editor_data[target]

        store.layout_editor_target = target
        store.layout_editor_x = data["x"]
        store.layout_editor_y = data["y"]
        store.layout_editor_zoom = data["zoom"]


    def layout_editor_dragged(drags, drop):

        if not drags:
            return

        drag = drags[0]

        x = drag.x / config.screen_width
        y = drag.y / config.screen_height

        store.layout_editor_x = max(0.0, min(1.0, x))
        store.layout_editor_y = max(0.0, min(1.0, y))

        data = layout_editor_data[store.layout_editor_target]

        data["x"] = store.layout_editor_x
        data["y"] = store.layout_editor_y

        renpy.restart_interaction()


    def layout_editor_change_zoom(amount):

        zoom = store.layout_editor_zoom + amount

        zoom = max(0.20, min(1.50, zoom))

        store.layout_editor_zoom = zoom

        layout_editor_data[
            store.layout_editor_target
        ]["zoom"] = zoom

        renpy.restart_interaction()


    def layout_editor_set_zoom(value):

        store.layout_editor_zoom = value

        layout_editor_data[
            store.layout_editor_target
        ]["zoom"] = value

        renpy.restart_interaction()


    def layout_editor_code():

        data = layout_editor_data[store.layout_editor_target]

        crop_code = ""

        if data["crop"] is not None:
            crop_code = "    crop {}\n".format(data["crop"])

        return (
            "transform {}_layout:\n"
            "{}"
            "    xanchor 0.5\n"
            "    xpos {:.3f}\n"
            "    yanchor 1.0\n"
            "    ypos {:.3f}\n"
            "    zoom {:.3f}"
        ).format(
            store.layout_editor_target,
            crop_code,
            data["x"],
            data["y"],
            data["zoom"]
        )


screen layout_editor():

    modal True

    add "ch1_dialogue"


    frame:
        xalign 0.5
        yalign 0.03

        padding (15, 10)

        text "LAYOUT EDITOR":
            size 28
            bold True


    frame:

        xpos 0.03
        ypos 0.10

        xsize 220
        ysize 600

        padding (15, 15)

        vbox:

            spacing 8

            text "CHARACTER":
                size 20
                bold True

            textbutton "MC":
                action Function(layout_editor_select, "mc")

            textbutton "Cory":
                action Function(layout_editor_select, "cory")

            textbutton "Bass":
                action Function(layout_editor_select, "bass")

            textbutton "Uceng":
                action Function(layout_editor_select, "uceng")

            textbutton "Lele":
                action Function(layout_editor_select, "lele")

            textbutton "Gator":
                action Function(layout_editor_select, "gator")


    drag:

        drag_name "character"

        draggable True

        xpos int(layout_editor_x * config.screen_width)
        ypos int(layout_editor_y * config.screen_height)

        add layout_editor_data[layout_editor_target]["image"]:

            xanchor 0.5
            yanchor 1.0

            if layout_editor_data[layout_editor_target]["crop"] is not None:
                crop layout_editor_data[layout_editor_target]["crop"]

            zoom layout_editor_zoom

        dragged layout_editor_dragged


    frame:

        xpos 0.72
        ypos 0.10

        xsize 0.25
        ysize 600

        padding (20, 20)

        vbox:

            spacing 12

            text "POSITION":
                size 20
                bold True

            text "X: [layout_editor_x:.3f]"
            text "Y: [layout_editor_y:.3f]"

            text "SIZE":
                size 20
                bold True

            text "Zoom: [layout_editor_zoom:.3f]"

            hbox:

                spacing 15

                textbutton "-":
                    action Function(layout_editor_change_zoom, -0.05)

                bar:

                    value VariableValue(
                        "layout_editor_zoom",
                        1.50,
                        offset=0.20
                    )

                    changed Function(
                        layout_editor_set_zoom,
                        layout_editor_zoom
                    )

                    xmaximum 250

                textbutton "+":
                    action Function(layout_editor_change_zoom, 0.05)


            text "− / + untuk ukuran":
                size 16


            null height 20


            text "TRANSFORM CODE":
                size 20
                bold True


            frame:

                xfill True

                padding (10, 10)

                text layout_editor_code():
                    size 13


            null height 20

            textbutton "CLOSE":
                action Hide("layout_editor")