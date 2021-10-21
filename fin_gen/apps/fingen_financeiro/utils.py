from datetime import date
from types import FunctionType
from typing import Dict, Iterable, Optional, Tuple

from fin_gen.apps.fingen_atividade.models import Atividade
from fin_gen.apps.fingen_atividade.models.categoria import Categoria


def group_atividades_by_month(objects: Iterable[Atividade]) -> Dict:
    group = {}
    for obj in objects:
        key = f'{obj.data_da_atividade.year}-{obj.data_da_atividade.month}'
        if group.get(key, None) is None:
            group[key] = [obj]
        else:
            group[key].append(obj)
    return group


def group_atividades_by_year(objects: Iterable[Atividade]) -> Dict:
    group = {}
    for obj in objects:
        key = f'{obj.data_da_atividade.year}'
        if group.get(key, None) is None:
            group[key] = [obj]
        else:
            group[key].append(obj)
    return group


def atividades_mean(objects: Dict or None) -> float:
    value = sum([y.valor for x in objects.values() for y in x])
    
    return round(value / len(objects), 2)


def group_atividades_by_selected_year(objects: Iterable[Atividade], year: int = date.today().year) -> Dict:
    group = {}
    for obj in objects:
        if obj.data_da_atividade.year == year:
            year_key = f'{year}'
            month_key = f'{obj.data_da_atividade.month}'
            if group.get(year_key, None) is None:
                group[year_key] = {
                    month_key: float(obj.valor)
                }
            else:
                if group[year_key].get(month_key, None) is None:
                    group[year_key].update({
                        month_key: float(obj.valor)
                    })
                else:
                    group[year_key][month_key] += float(obj.valor)
    if len(group) == 1:
        for i in range(1, 13):
            if f'{i}' in group[f'{year}']:
                continue
            else:
                group[year_key][f'{i}'] = 0

        group[year_key] = {x[0]: x[1] for x in sorted(group[year_key].items(), key=lambda x: int(x[0]))}
    return group


def atitivades_categories_percentage(objects: Iterable[Atividade]) -> Iterable[Tuple[str, float, str]]:
    group = {}
    total_atividades = len(objects)
    for obj in objects:
        key = f'{obj.categoria.titulo}'
        if group.get(key, None) is None:
            group[key] = 1
        else:
            group[key] += 1
    return [(k, round(v/total_atividades * 100 , 2), Categoria.objects.get(titulo=k).cor) for k, v in group.items()]


def is_empty(objects: Iterable[Atividade], cb: FunctionType, **cb_params):
    if objects is None:
        return None
    result = len(objects) > 0
    if result:
        return cb(objects, **cb_params)
    return None
