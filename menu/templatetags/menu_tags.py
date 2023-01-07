from django import template
from menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, name_menu):
    try:
        items = MenuItem.objects.filter(menu__title=name_menu)
        items_values = list(items)
        primary_item = [item for item in items_values if item.parent_id is None]
        selected_item_slug = context['request'].build_absolute_uri().split('/')[-1]
        selected_item = None

        for i in items_values:
            if i.slug == selected_item_slug:
                selected_item = i
        selected_item_slug_list = get_selected_item_slug_list(selected_item, items_values)

        for item in primary_item:
            if item.slug in selected_item_slug_list:
                item.child_items = get_child_items(items_values, item.id, selected_item_slug_list)
        result_dict = {'items': primary_item}

    except:
        result_dict = {
            'items': [
                item for item in MenuItem.objects.filter(menu__title=name_menu, parent=None).values()
            ]
        }

    return result_dict


def get_child_items(items_values, item_id, selected_item_slug_list):
    item_list = [item for item in items_values if item.parent_id is item_id]
    for item in item_list:
        if item.slug in selected_item_slug_list:
            item.child_items = get_child_items(items_values, item.id, selected_item_slug_list)
    return item_list


def get_selected_item_slug_list(selected_item, items_values):
    selected_item_slug_list = []

    while selected_item:
        selected_item_slug_list.append(selected_item.slug)
        if selected_item.parent_id:
            for i in items_values:
                if i.id == selected_item.parent_id:
                    selected_item = i
        else:
            selected_item = None
    return selected_item_slug_list
