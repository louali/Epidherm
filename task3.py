def FilterMaterials(materials, family_id='', m_comb_max='',  m_comb_min='', m_surf_max='',  m_surf_min=''):
    if m_comb_max != '':
        materials = [i for i in materials if not (i['details']['masse_combustible'] > m_comb_max)]
    if family_id != '':
        materials = [i for i in materials if not (i['family']['id'] != family_id)]
    if m_comb_min != '':
        materials = [i for i in materials if not (i['details']['masse_combustible'] < m_comb_min)]
    if m_surf_max != '':
        materials = [i for i in materials if not (i['details']['masse_surfacique'] > m_surf_max)]
    if m_surf_min != '':
        materials = [i for i in materials if not (i['details']['masse_surfacique'] < m_surf_min)]
    return(materials)