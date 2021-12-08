
canvas_path = "assets/sprites/ui/"


def get_item_by_id(id):

    switcher = {

        # Sunflower
        1: "assets/sprites/environment/sunflower/sunflower1.png",

        # Other
        2: "assets/sprites/environment/cloud.png"
    }

    return switcher.get(id, "")

