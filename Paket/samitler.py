def samitleri_al(cumle):
    samitler = set()
    for herf in cumle:
        if herf.lower() not in 'aıoueəiöü' and herf.lower() != ' ':
            samitler.add(herf)
    return samitler
