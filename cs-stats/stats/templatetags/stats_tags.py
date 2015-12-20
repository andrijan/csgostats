from django.template import Library

register = Library()

@register.filter
def add_remove_id(url_params, player_id):
    """
    params is a parameter to replace
    """
    player_ids = url_params.get('ids', [])
    player_ids = player_ids.split(',') if player_ids else []
    player_id = str(player_id)
    if player_id in player_ids:
        player_ids.remove(player_id)
    else:
        player_ids.append(player_id)
    return ",".join(player_ids)
