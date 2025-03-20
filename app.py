from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- Gene: Extension ----------------
def vererbung_extension(ex_vater, ex_mutter):
    possible_ex_fohlen = set()
    if ex_vater == "EE" and ex_mutter == "EE":
        possible_ex_fohlen = ["EE"]
    elif ex_vater == "EE" and ex_mutter == "Ee":
        possible_ex_fohlen = ["EE", "Ee"]
    elif ex_vater == "EE" and ex_mutter == "eE":
        possible_ex_fohlen = ["EE", "Ee"]
    elif ex_vater == "EE" and ex_mutter == "ee":
        possible_ex_fohlen = ["Ee"]
    elif ex_vater == "Ee" and ex_mutter == "EE":
        possible_ex_fohlen = ["EE", "eE"]
    elif ex_vater == "Ee" and ex_mutter == "Ee":
        possible_ex_fohlen = ["EE", "Ee"]
    elif ex_vater == "Ee" and ex_mutter == "eE":
        possible_ex_fohlen = ["EE", "Ee", "ee", "eE"]
    elif ex_vater == "Ee" and ex_mutter == "ee":
        possible_ex_fohlen = ["Ee", "ee"]
    elif ex_vater == "eE" and ex_mutter == "EE":
        possible_ex_fohlen = ["eE", "EE"]
    elif ex_vater == "eE" and ex_mutter == "Ee":
        possible_ex_fohlen = ["EE", "Ee", "ee", "eE"]
    elif ex_vater == "eE" and ex_mutter == "eE":
        possible_ex_fohlen = ["EE", "Ee", "ee", "eE"]
    elif ex_vater == "eE" and ex_mutter == "ee":
        possible_ex_fohlen = ["Ee", "ee"]
    elif ex_vater == "ee" and ex_mutter == "EE":
        possible_ex_fohlen = ["eE"]
    elif ex_vater == "ee" and ex_mutter == "Ee":
        possible_ex_fohlen = ["eE", "ee"]
    elif ex_vater == "ee" and ex_mutter == "eE":
        possible_ex_fohlen = ["eE", "ee"]
    elif ex_vater == "ee" and ex_mutter == "ee":
        possible_ex_fohlen = ["ee"]
    return list(possible_ex_fohlen)

# ---------------- Gene: Agouti ----------------
def vererbung_agouti(ag_vater, ag_mutter):
    possible_ag_fohlen = set()
    if len(ag_vater) == 4 and len(ag_mutter) == 4:
        ag_vater_allele = [ag_vater[0:2], ag_vater[2:4]]
        ag_mutter_allele = [ag_mutter[0:2], ag_mutter[2:4]]
        allele_combinations = [
            (ag_vater_allele[0], ag_mutter_allele[0]),
            (ag_vater_allele[0], ag_mutter_allele[1]),
            (ag_vater_allele[1], ag_mutter_allele[0]),
            (ag_vater_allele[1], ag_mutter_allele[1]),
        ]
        for father, mother in allele_combinations:
            if father == "Ap" and mother == "Ap":
                possible_ag_fohlen.add("Ap+Ap")
            elif father == "Ap" and mother == "A1":
                possible_ag_fohlen.add("Ap+A1")
            elif father == "A1" and mother == "Ap":
                possible_ag_fohlen.add("Ap+A1")
            elif father == "Ap" and mother == "At":
                possible_ag_fohlen.add("Ap+At")
            elif father == "At" and mother == "Ap":
                possible_ag_fohlen.add("Ap+At")
            elif father == "Ap" and mother == "a0":
                possible_ag_fohlen.add("Ap+a0")
            elif father == "a0" and mother == "Ap":
                possible_ag_fohlen.add("Ap+a0")
            elif father == "A1" and mother == "A1":
                possible_ag_fohlen.add("A1+A1")
            elif father == "A1" and mother == "At":
                possible_ag_fohlen.add("A1+At")
            elif father == "At" and mother == "A1":
                possible_ag_fohlen.add("A1+At")
            elif father == "A1" and mother == "a0":
                possible_ag_fohlen.add("A1+a0")
            elif father == "a0" and mother == "A1":
                possible_ag_fohlen.add("A1+a0")
            elif father == "At" and mother == "At":
                possible_ag_fohlen.add("At+At")
            elif father == "At" and mother == "a0":
                possible_ag_fohlen.add("At+a0")
            elif father == "a0" and mother == "At":
                possible_ag_fohlen.add("At+a0")
            elif father == "a0" and mother == "a0":
                possible_ag_fohlen.add("a0+a0")
    return list(possible_ag_fohlen)

# ---------------- Gene: Dun ----------------
def vererbung_dun(dun_vater, dun_mutter):
    """
    Liefert alle möglichen Dun-Genotypen des Fohlens,
    basierend auf den Eingaben (dd, Dd, dD, DD) für Vater und Mutter.
    """
    possible_dun_fohlen = set()

    # (dd, dd)
    if dun_vater == "dd" and dun_mutter == "dd":
        possible_dun_fohlen.update(["dd"])
    # (dd, Dd)
    elif dun_vater == "dd" and dun_mutter == "Dd":
        possible_dun_fohlen.update(["dd", "dD"])
    # (dd, dD)
    elif dun_vater == "dd" and dun_mutter == "dD":
        possible_dun_fohlen.update(["dd", "dD"])
    # (dd, DD)
    elif dun_vater == "dd" and dun_mutter == "DD":
        possible_dun_fohlen.update(["dD"])

    # (Dd, dd)
    elif dun_vater == "Dd" and dun_mutter == "dd":
        possible_dun_fohlen.update(["dd", "Dd"])
    # (Dd, Dd)
    elif dun_vater == "Dd" and dun_mutter == "Dd":
        possible_dun_fohlen.update(["DD", "Dd", "dD", "dd"])
    # (Dd, dD)
    elif dun_vater == "Dd" and dun_mutter == "dD":
        possible_dun_fohlen.update(["DD", "Dd", "dD", "dd"])
    # (Dd, DD)
    elif dun_vater == "Dd" and dun_mutter == "DD":
        possible_dun_fohlen.update(["DD", "dD"])

    # (dD, dd)
    elif dun_vater == "dD" and dun_mutter == "dd":
        possible_dun_fohlen.update(["dd", "Dd"])
    # (dD, Dd)
    elif dun_vater == "dD" and dun_mutter == "Dd":
        possible_dun_fohlen.update(["DD", "Dd", "dD", "dd"])
    # (dD, dD)
    elif dun_vater == "dD" and dun_mutter == "dD":
        possible_dun_fohlen.update(["DD", "Dd", "dD", "dd"])
    # (dD, DD)
    elif dun_vater == "dD" and dun_mutter == "DD":
        possible_dun_fohlen.update(["DD", "dD"])

    # (DD, dd)
    elif dun_vater == "DD" and dun_mutter == "dd":
        possible_dun_fohlen.update(["Dd"])
    # (DD, Dd)
    elif dun_vater == "DD" and dun_mutter == "Dd":
        possible_dun_fohlen.update(["DD", "Dd"])
    # (DD, dD)
    elif dun_vater == "DD" and dun_mutter == "dD":
        possible_dun_fohlen.update(["DD", "dD"])
    # (DD, DD)
    elif dun_vater == "DD" and dun_mutter == "DD":
        possible_dun_fohlen.update(["DD"])

    return list(possible_dun_fohlen)

# ---------------- Gene: Cream ----------------
def vererbung_cream(cr_vater, cr_mutter):
    """
    Liefert alle möglichen Cream-Genotypen des Fohlens,
    basierend auf den Eingaben (crcr, Crcr, crCr, CrCr) für Vater und Mutter.
    """
    possible_cr_fohlen = set()

    # (crcr, crcr)
    if cr_vater == "crcr" and cr_mutter == "crcr":
        possible_cr_fohlen.update(["crcr"])
    # (crcr, Crcr)
    elif cr_vater == "crcr" and cr_mutter == "Crcr":
        possible_cr_fohlen.update(["Crcr", "crcr"])
    # (crcr, crCr)
    elif cr_vater == "crcr" and cr_mutter == "crCr":
        possible_cr_fohlen.update(["Crcr", "crcr"])
    # (crcr, CrCr)
    elif cr_vater == "crcr" and cr_mutter == "CrCr":
        possible_cr_fohlen.update(["CrCr"])

    # (Crcr, crcr)
    elif cr_vater == "Crcr" and cr_mutter == "crcr":
        possible_cr_fohlen.update(["Crcr", "crcr"])
    # (Crcr, Crcr)
    elif cr_vater == "Crcr" and cr_mutter == "Crcr":
        # Alle vier möglich: CrCr, Crcr, crCr, crcr
        possible_cr_fohlen.update(["CrCr", "Crcr", "crCr", "crcr"])
    # (Crcr, crCr)
    elif cr_vater == "Crcr" and cr_mutter == "crCr":
        possible_cr_fohlen.update(["CrCr", "Crcr", "crCr", "crcr"])
    # (Crcr, CrCr)
    elif cr_vater == "Crcr" and cr_mutter == "CrCr":
        possible_cr_fohlen.update(["CrCr", "crCr"])

    # (crCr, crcr)
    elif cr_vater == "crCr" and cr_mutter == "crcr":
        possible_cr_fohlen.update(["Crcr", "crcr"])
    # (crCr, Crcr)
    elif cr_vater == "crCr" and cr_mutter == "Crcr":
        possible_cr_fohlen.update(["CrCr", "Crcr", "crCr", "crcr"])
    # (crCr, crCr)
    elif cr_vater == "crCr" and cr_mutter == "crCr":
        possible_cr_fohlen.update(["CrCr", "crCr", "Crcr", "crcr"])
    # (crCr, CrCr)
    elif cr_vater == "crCr" and cr_mutter == "CrCr":
        possible_cr_fohlen.update(["CrCr", "crCr"])

    # (CrCr, crcr)
    elif cr_vater == "CrCr" and cr_mutter == "crcr":
        possible_cr_fohlen.update(["CrCr"])
    # (CrCr, Crcr)
    elif cr_vater == "CrCr" and cr_mutter == "Crcr":
        possible_cr_fohlen.update(["CrCr", "crCr"])
    # (CrCr, crCr)
    elif cr_vater == "CrCr" and cr_mutter == "crCr":
        possible_cr_fohlen.update(["CrCr", "crCr"])
    # (CrCr, CrCr)
    elif cr_vater == "CrCr" and cr_mutter == "CrCr":
        possible_cr_fohlen.update(["CrCr"])

    return list(possible_cr_fohlen)

# ---------------- Gene: Champagne ----------------
def vererbung_champagne(ch_vater, ch_mutter):
    possibilities = set()
    if ch_vater == "ChCh" and ch_mutter == "ChCh":
        possibilities.add("ChCh")
    elif (ch_vater == "ChCh" and ch_mutter == "Chch") or (ch_vater == "ChCh" and ch_mutter == "chCh"):
        possibilities.update(["ChCh", "Chch"])
    elif (ch_vater == "ChCh" and ch_mutter == "chch"):
        possibilities.add("Chch")
    elif (ch_vater == "Chch" and ch_mutter == "Chch") or (ch_vater == "Chch" and ch_mutter == "chCh"):
        possibilities.update(["Chch", "ChCh", "chch", "chCh"])
    elif (ch_vater == "Chch" and ch_mutter == "chch"):
        possibilities.update(["Chch", "chch"])
    elif (ch_vater == "chCh" and ch_mutter == "Chch") or (ch_vater == "chCh" and ch_mutter == "chCh"):
        possibilities.update(["Chch", "ChCh", "chch", "chCh"])
    elif (ch_vater == "chCh" and ch_mutter == "chch"):
        possibilities.update(["Chch", "chch"])
    elif (ch_vater == "chch" and ch_mutter == "Chch") or (ch_vater == "chch" and ch_mutter == "chCh"):
        possibilities.update(["chch", "chCh"])
    elif (ch_vater == "Chch" and ch_mutter == "ChCh") or (ch_vater == "chCh" and ch_mutter == "ChCh"):
        possibilities.update(["ChCh", "chCh"])
    elif (ch_vater == "chch" and ch_mutter == "ChCh"):
        possibilities.update(["chCh"])
    elif (ch_vater == "Chch" and ch_mutter == "Chch") or (ch_vater == "chCh" and ch_mutter == "Chch"):
        possibilities.update(["ChCh", "chCh", "chch", "Chch"])
    elif (ch_vater == "chch" and ch_mutter == "Chch"):
        possibilities.update(["chCh", "chch"])
    elif (ch_vater == "Chch" and ch_mutter == "chCh") or (ch_vater == "chCh" and ch_mutter == "chCh"):
        possibilities.update(["ChCh", "chCh", "chch", "Chch"])
    elif (ch_vater == "chch" and ch_mutter == "chCh"):
        possibilities.update(["chCh", "chch"])
    elif (ch_vater == "Chch" and ch_mutter == "chch") or (ch_vater == "chCh" and ch_mutter == "chch"):
        possibilities.update(["Chch", "chch"])
    else:
        possibilities.add("chch")
    return list(possibilities)

def apply_champagne_effect(end_colors, ch_combination):
    new_colors = []
    if any(genotype != "chch" for genotype in ch_combination):
        for color in end_colors:
            if color == "Chestnut":
                new_colors.append("Gold Champagne Chestnut")
            elif color in ["Wildbay", "Bay"]:
                new_colors.append("Amber Champagne Bay")
            elif color == "Sealbrown":
                new_colors.append("Sable Champagne Sealbrown")
            elif color == "Black":
                new_colors.append("Classic Champagne Black")
            else:
                new_colors.append("Champagne " + color)
    return list(set(end_colors + new_colors))

# ---------------- Gene: Grey ----------------
def vererbung_grey(g_vater, g_mutter):
    if len(g_vater) != 2 or len(g_mutter) != 2:
        return []
    possibilities = set()
    for allele_v in g_vater:
        for allele_m in g_mutter:
            possibilities.add(allele_v + allele_m)
    return list(possibilities)

def apply_grey_effect(end_colors, grey_combination):
    if all(g == "gg" for g in grey_combination):
        return end_colors
    elif all(g != "gg" for g in grey_combination):
        return ["Grey"]
    else:
        return list(set(end_colors + ["Grey"]))

# ---------------- Gene: Kit ----------------
def vererbung_kit(kit_vater, kit_mutter):
    if len(kit_vater) != 4 or len(kit_mutter) != 4:
        return []
    vater_allele = [kit_vater[0:2], kit_vater[2:4]]
    mutter_allele = [kit_mutter[0:2], kit_mutter[2:4]]
    possibilities = set()
    for a in vater_allele:
        for b in mutter_allele:
            geno = a + b
            if geno == "WIWI":
                continue  # lethaler Fall
            possibilities.add(geno)
    return list(possibilities)

def kit_effect(kit_genotype):
    if kit_genotype == "0000":
        return ""
    allele1 = kit_genotype[:2]
    allele2 = kit_genotype[2:]
    if allele1.startswith("WI") or allele2.startswith("WI"):
        return "White"
    def allele_effect(allele):
        if allele == "00":
            return ""
        if allele.startswith("TO"):
            return "Tobiano"
        if allele.startswith("SB"):
            return "Sabino"
        if allele.startswith("Rn") or allele.startswith("RN"):
            return "Roan"
        return ""
    eff1 = allele_effect(allele1)
    eff2 = allele_effect(allele2)
    if eff1 and eff2:
        if eff1 == eff2:
            return eff1
        else:
            return " ".join(sorted([eff1, eff2]))
    elif eff1:
        return eff1
    elif eff2:
        return eff2
    else:
        return ""

def apply_kit_effect(end_colors, kit_combinations):
    kit_effects = set()
    for geno in kit_combinations:
        eff = kit_effect(geno)
        kit_effects.add(eff)
    result = set()
    for color in end_colors:
        for eff in kit_effects:
            if eff:
                result.add(color + " " + eff)
            else:
                result.add(color)
    return list(result)

# ---------------- Gene: Silver ----------------
def vererbung_silver(z_vater, z_mutter):
    if len(z_vater) != 2 or len(z_mutter) != 2:
        return []
    possibilities = set()
    for allele_v in z_vater:
        for allele_m in z_mutter:
            possibilities.add(allele_v + allele_m)
    return list(possibilities)

def apply_silver_effect(end_colors, silver_combination):
    if not any("Z" in genotype for genotype in silver_combination):
        return end_colors
    else:
        result = []
        for color in end_colors:
            if color.lower() == "chestnut":
                result.append(color)
            else:
                result.append("Silver " + color)
        return list(set(result + end_colors))

# ---------------- Gene: Overo ----------------
def vererbung_overo(o_vater, o_mutter):
    if len(o_vater) != 2 or len(o_mutter) != 2:
        return []
    possibilities = set()
    for allele_v in o_vater:
        for allele_m in o_mutter:
            possibilities.add(allele_v + allele_m)
    return list(possibilities)

def apply_overo_effect(end_colors, overo_combination):
    if "OO" in overo_combination:
        return ["Overo (Lethal)"]
    elif any(g == "Oo" for g in overo_combination):
        return [color + " Overo" for color in end_colors]
    else:
        return end_colors

# ---------------- Gene: Splashed White ----------------
def vererbung_splashed_white(spl_vater, spl_mutter):
    if len(spl_vater) != 6 or len(spl_mutter) != 6:
        return []
    alleles_v = [spl_vater[:3], spl_vater[3:]]
    alleles_m = [spl_mutter[:3], spl_mutter[3:]]
    possibilities = set()
    for a in alleles_v:
        for b in alleles_m:
            possibilities.add(a + b)
    return list(possibilities)

def splashed_white_effect(spl_genotype):
    if spl_genotype == "splspl":
        return ""
    else:
        return "Splashed White"

def apply_splashed_white_effect(end_colors, spl_white_combinations):
    # Falls mindestens eine Kombination nicht "splspl" ist,
    # hänge den Effekt "Splashed White" an alle Endfarben an.
    if not all(geno == "splspl" for geno in spl_white_combinations):
        return [color + " Splashed White" for color in end_colors]
    else:
        return end_colors

# ---------------- Gene: LP und PATN1 ----------------
def vererbung_lp(lp_vater, lp_mutter):
    possible_lp_fohlen = []
    if lp_vater == "LPLP" and lp_mutter == "LPLP":
        possible_lp_fohlen = ["LPLP"]
    elif lp_vater == "LPLP" and lp_mutter == "LPlp":
        possible_lp_fohlen = ["LPLP", "LPlp"]
    elif lp_vater == "LPLP" and lp_mutter == "lpLP":
        possible_lp_fohlen = ["LPLP", "LPlp", "lpLP"]
    elif lp_vater == "LPLP" and lp_mutter == "lplp":
        possible_lp_fohlen = ["LPLP", "LPlp"]
    elif lp_vater == "LPlp" and lp_mutter == "LPLP":
        possible_lp_fohlen = ["LPLP", "LPlp"]
    elif lp_vater == "LPlp" and lp_mutter == "LPlp":
        possible_lp_fohlen = ["LPLP", "LPlp", "lpLP", "lplp"]
    elif lp_vater == "LPlp" and lp_mutter == "lpLP":
        possible_lp_fohlen = ["LPLP", "LPlp", "lpLP", "lplp"]
    elif lp_vater == "LPlp" and lp_mutter == "lplp":
        possible_lp_fohlen = ["LPLP", "LPlp", "lplp"]
    elif lp_vater == "lpLP" and lp_mutter == "LPLP":
        possible_lp_fohlen = ["lpLP", "LPLP"]
    elif lp_vater == "lpLP" and lp_mutter == "LPlp":
        possible_lp_fohlen = ["lpLP", "LPlp", "lplp", "LPLP"]
    elif lp_vater == "lpLP" and lp_mutter == "lpLP":
        possible_lp_fohlen = ["lplp", "LPlp", "LPLP", "lpLP"]
    elif lp_vater == "lpLP" and lp_mutter == "lplp":
        possible_lp_fohlen = ["lpLP", "lplp"]
    elif lp_vater == "lplp" and lp_mutter == "LPLP":
        possible_lp_fohlen = ["lplp", "lpLP"]
    elif lp_vater == "lplp" and lp_mutter == "LPlp":
        possible_lp_fohlen = ["lplp", "lpLP", "LPLP"]
    elif lp_vater == "lplp" and lp_mutter == "lpLP":
        possible_lp_fohlen = ["lplp", "LPlp"]
    elif lp_vater == "lplp" and lp_mutter == "lplp":
        possible_lp_fohlen = ["lplp"]
    return possible_lp_fohlen

def vererbung_patn1(patn1_vater, patn1_mutter):
    possible_patn1_fohlen = []
    if patn1_vater == "P1P1" and patn1_mutter == "P1P1":
        possible_patn1_fohlen = ["P1P1"]
    elif patn1_vater == "P1P1" and patn1_mutter == "P1p1":
        possible_patn1_fohlen = ["P1P1", "P1p1"]
    elif patn1_vater == "P1P1" and patn1_mutter == "p1P1":
        possible_patn1_fohlen = ["P1P1", "P1p1"]
    elif patn1_vater == "P1P1" and patn1_mutter == "p1p1":
        possible_patn1_fohlen = ["P1p1"]
    elif patn1_vater == "P1p1" and patn1_mutter == "P1P1":
        possible_patn1_fohlen = ["P1P1", "P1p1"]
    elif patn1_vater == "P1p1" and patn1_mutter == "P1p1":
        possible_patn1_fohlen = ["P1P1", "P1p1", "p1P1", "p1p1"]
    elif patn1_vater == "P1p1" and patn1_mutter == "p1P1":
        possible_patn1_fohlen = ["P1P1", "P1p1", "p1P1", "p1p1"]
    elif patn1_vater == "P1p1" and patn1_mutter == "p1p1":
        possible_patn1_fohlen = ["P1p1", "p1p1"]
    elif patn1_vater == "p1P1" and patn1_mutter == "P1P1":
        possible_patn1_fohlen = ["p1P1", "P1P1"]
    elif patn1_vater == "p1P1" and patn1_mutter == "P1p1":
        possible_patn1_fohlen = ["p1P1", "P1P1", "P1p1", "p1p1"]
    elif patn1_vater == "p1P1" and patn1_mutter == "p1P1":
        possible_patn1_fohlen = ["p1p1", "P1p1"]
    elif patn1_vater == "p1P1" and patn1_mutter == "p1p1":
        possible_patn1_fohlen = ["p1P1"]
    elif patn1_vater == "p1p1" and patn1_mutter == "P1P1":
        possible_patn1_fohlen = ["p1P1"]
    elif patn1_vater == "p1p1" and patn1_mutter == "P1p1":
        possible_patn1_fohlen = ["p1P1", "p1p1"]
    elif patn1_vater == "p1p1" and patn1_mutter == "p1P1":
        possible_patn1_fohlen = ["p1P1", "p1p1"]
    elif patn1_vater == "p1p1" and patn1_mutter == "p1p1":
        possible_patn1_fohlen = ["p1p1"]
    return possible_patn1_fohlen

def apply_lp_patn1_effect(end_colors, lp_genotypes, patn1_genotypes):
    result = set()
    dominant_patn1 = {"P1P1", "P1p1", "p1P1"}
    for lp in lp_genotypes:
        for pat in patn1_genotypes:
            if lp == "LPLP":
                if pat in dominant_patn1:
                    effect = "Few Spot"
                else:
                    effect = "Snowcap"
            elif lp in ["LPlp", "lpLP"]:
                if pat in dominant_patn1:
                    effect = "Leopard"
                else:
                    effect = "Schabrackentiger"
            else:
                effect = ""
            if effect:
                for color in end_colors:
                    result.add(f"{color} {effect}")
            else:
                result.update(end_colors)
    return list(result)

# ---------------- Gruppierung ----------------
def gruppiere_und_sortiere_farben(final_colors):
    gruppen = {}
    for farbe in final_colors:
        basis = farbe.split()[0]
        gruppen.setdefault(basis, []).append(farbe)
    return gruppen

def bestimme_basisfarbe(ex_combination, ag_combination):
    basisfarben = []
    if ex_combination == "ee":
        basisfarben.append("Chestnut")
    elif ex_combination in ["EE", "Ee", "eE"]:
        if ag_combination == "a0+a0":
            basisfarben.append("Black")
        elif ag_combination == "Ap+Ap":
            basisfarben.append("Wildbay")
        elif ag_combination in ["Ap+A1", "A1+Ap", "Ap+At", "At+Ap", "Ap+a0", "a0+Ap"]:
            basisfarben.append("Wildbay")
        elif ag_combination == "A1+A1":
            basisfarben.append("Bay")
        elif ag_combination in ["A1+At", "At+A1", "A1+a0", "a0+A1"]:
            basisfarben.append("Bay")
        elif ag_combination == "At+At":
            basisfarben.append("Sealbrown")
        elif ag_combination in ["At+a0", "a0+At"]:
            basisfarben.append("Sealbrown")
    return basisfarben

def berechne_ende_gueltige_farbe(moegliche_basisfarben, cr_combination, dun_combination):
    finale_farben = []
    if any("D" in genotype for genotype in dun_combination):
        for farbe in moegliche_basisfarben:
            if farbe == "Chestnut":
                finale_farben.append("Red Dun")
                if any(x in cr_combination for x in ["CrCr", "Crcr", "crCr"]):
                    finale_farben.append("Dunalino")
            elif farbe in ["Bay", "Wildbay"]:
                finale_farben.append("Classic Dun")
                if any(x in cr_combination for x in ["CrCr", "Crcr", "crCr"]):
                    finale_farben.append("Dunskin")
            elif farbe == "Sealbrown":
                finale_farben.append("Brown Dun")
            elif farbe == "Black":
                finale_farben.append("Grulla")
                if any(x in cr_combination for x in ["CrCr", "Crcr", "crCr"]):
                    finale_farben.append("Smoky Grulla")
    for farbe in moegliche_basisfarben:
        finale_farben.append(farbe)
        if "CrCr" in cr_combination:
            if farbe == "Chestnut":
                finale_farben.append("Cremello")
            elif farbe in ["Wildbay", "Bay"]:
                finale_farben.append("Perlino")
            elif farbe == "Sealbrown":
                finale_farben.append("SealBrown Cream")
            elif farbe == "Black":
                finale_farben.append("Smoky Cream")
        if "Crcr" in cr_combination or "crCr" in cr_combination:
            if farbe == "Chestnut":
                finale_farben.append("Palomino")
            elif farbe in ["Wildbay", "Bay"]:
                finale_farben.append("Buckskin")
            elif farbe == "Sealbrown":
                finale_farben.append("Smoky Brown")
            elif farbe == "Black":
                finale_farben.append("Smoky Black")
    return list(set(finale_farben))

# ---------------- Hauptfunktion ----------------
def berechne_fohlenfarbe(
    ex_vater, ex_mutter, ag_vater, ag_mutter, dun_vater, dun_mutter,
    cr_vater, cr_mutter, ch_vater, ch_mutter, g_vater, g_mutter,
    kit_vater, kit_mutter, z_vater, z_mutter, o_vater, o_mutter,
    spl_vater, spl_mutter, lp_vater, lp_mutter, patn1_vater, patn1_mutter
):
    possible_ex_fohlen = vererbung_extension(ex_vater, ex_mutter)
    possible_ag_fohlen = vererbung_agouti(ag_vater, ag_mutter)
    possible_dun_fohlen = vererbung_dun(dun_vater, dun_mutter)
    possible_cr_fohlen = vererbung_cream(cr_vater, cr_mutter)
    possible_champagne = vererbung_champagne(ch_vater, ch_mutter)
    possible_grey = vererbung_grey(g_vater, g_mutter)
    possible_kit = vererbung_kit(kit_vater, kit_mutter)
    possible_silver = vererbung_silver(z_vater, z_mutter)
    possible_overo = vererbung_overo(o_vater, o_mutter)
    possible_splashed_white = vererbung_splashed_white(spl_vater, spl_mutter)

    moegliche_basisfarben = []
    for ex in possible_ex_fohlen:
        for ag in possible_ag_fohlen:
            moegliche_basisfarben.extend(bestimme_basisfarbe(ex, ag))
    moegliche_basisfarben = list(set(moegliche_basisfarben))

    moegliche_endfarben = berechne_ende_gueltige_farbe(moegliche_basisfarben, possible_cr_fohlen, possible_dun_fohlen)
    finale_farben = apply_champagne_effect(moegliche_endfarben, possible_champagne)
    finale_farben = apply_silver_effect(finale_farben, possible_silver)
    finale_farben = apply_grey_effect(finale_farben, possible_grey)
    finale_farben = apply_kit_effect(finale_farben, possible_kit)
    finale_farben = apply_overo_effect(finale_farben, possible_overo)
    finale_farben = apply_splashed_white_effect(finale_farben, possible_splashed_white)

    lp_fohlen = vererbung_lp(lp_vater, lp_mutter)
    patn1_fohlen = vererbung_patn1(patn1_vater, patn1_mutter)
    final_with_muster = apply_lp_patn1_effect(finale_farben, lp_fohlen, patn1_fohlen)

    gruppen_dict = gruppiere_und_sortiere_farben(final_with_muster)

    return {
        "extension": possible_ex_fohlen,
        "agouti": possible_ag_fohlen,
        "dun": possible_dun_fohlen,
        "cream": possible_cr_fohlen,
        "champagne": possible_champagne,
        "grey": possible_grey,
        "kit": possible_kit,
        "silver": possible_silver,
        "overo": possible_overo,
        "splashed_white": possible_splashed_white,
        "basisfarben": moegliche_basisfarben,
        "finale_farben": final_with_muster,
        "gruppen": gruppen_dict
    }

# ---------------- Flask-Route ----------------
@app.route("/", methods=["GET", "POST"])
def index():
    # Standardwerte definieren
    default_values = {
        "ex_vater": "ee",
        "ag_vater": "a0a0",
        "dun_vater": "dd",
        "cr_vater": "crcr",
        "ch_vater": "chch",
        "g_vater": "gg",
        "kit_vater": "0000",
        "z_vater": "zz",
        "o_vater": "oo",
        "spl_vater": "splspl",
        "lp_vater": "lplp",
        "patn1_vater": "p1p1",
        "ex_mutter": "ee",
        "ag_mutter": "a0a0",
        "dun_mutter": "dd",
        "cr_mutter": "crcr",
        "ch_mutter": "chch",
        "g_mutter": "gg",
        "kit_mutter": "0000",
        "z_mutter": "zz",
        "o_mutter": "oo",
        "spl_mutter": "splspl",
        "lp_mutter": "lplp",
        "patn1_mutter": "p1p1"
    }
    form_data = {}
    """
    Zeigt ein Formular mit zwei separaten Abschnitten:
    - alle Gene vom Vater
    - alle Gene von der Mutter
    """
    # 1) Dictionary nur für Vater-Gene
    gene_options_vater = {
        "ex_vater":  ["EE", "Ee", "eE", "ee"],
        "ag_vater":  ["ApAp", "A1A1", "AtAt", "a0a0", "ApA1", "A1Ap", "ApAt", "AtAp", "Apa0", "a0Ap", "A1At", "AtA1", "A1a0", "a0A1", "Ata0",           "a0At"],
        "dun_vater": ["dd", "DD", "Dd", "dD"],
        "cr_vater":  ["crcr", "CrCr", "Crcr", "crCr"],
        "ch_vater":  ["ChCh", "Chch", "chCh", "chch"],
        "g_vater":   ["gg", "Gg", "gG", "GG"],
        "kit_vater": ["0000", "TOTO", "TO00", "00TO", "RnRn", "Rn00", "00Rn", "SB00", "00SB", "SBSB", "WI00", "00WI", "TORn", "RnTO", "RnSB", "SBRn", "TOSB", "SBTO"],
        "z_vater":   ["zz", "zZ", "Zz", "ZZ"],
        "o_vater":   ["oo", "Oo", "oO", "OO"],
        "spl_vater": ["splspl", "SPLspl", "splSPL", "SPLSPL"],
        "lp_vater":  ["lplp", "LPlp", "lpLP", "LPLP"],
        "patn1_vater": ["p1p1", "P1p1", "p1P1", "P1P1"],
    }

    # 2) Dictionary nur für Mutter-Gene
    gene_options_mutter = {
        "ex_mutter":  ["EE", "Ee", "eE", "ee"],
        "ag_mutter": ["ApAp", "A1A1", "AtAt", "a0a0", "ApA1", "A1Ap", "ApAt", "AtAp", "Apa0", "a0Ap", "A1At", "AtA1", "A1a0", "a0A1", "Ata0",           "a0At"],
        "dun_mutter": ["dd", "DD", "Dd", "dD"],
        "cr_mutter":  ["crcr", "CrCr", "Crcr", "crCr"],
        "ch_mutter":  ["ChCh", "Chch", "chCh", "chch"],
        "g_mutter":   ["gg", "Gg", "gG", "GG"],
        "kit_mutter":["0000", "TOTO", "TO00", "00TO", "RnRn", "Rn00", "00Rn", "SB00", "00SB", "SBSB", "WI00", "00WI", "TORn", "RnTO", "RnSB", "SBRn", "TOSB", "SBTO"],
        "z_mutter":   ["zz", "zZ", "Zz", "ZZ"],
        "o_mutter":   ["oo", "Oo", "oO", "OO"],
        "spl_mutter": ["splspl", "SPLspl", "splSPL", "SPLSPL"],
        "lp_mutter":  ["lplp", "LPlp", "lpLP", "LPLP"],
        "patn1_mutter": ["p1p1", "P1p1", "p1P1", "P1P1"],
    }

    results = None

    # 3) POST: Daten einsammeln
    if request.method == "POST":
        form_data = {}

        # a) Alle Vater-Gene auslesen
        for gene in gene_options_vater.keys():
            form_data[gene] = request.form.get(gene, "")

        # b) Alle Mutter-Gene auslesen
        for gene in gene_options_mutter.keys():
            form_data[gene] = request.form.get(gene, "")

        # c) An deine Berechnungsfunktion übergeben
        #    Achte genau auf die Reihenfolge der Argumente:
        #    (ex_vater, ex_mutter, ag_vater, ag_mutter, usw.)
        results = berechne_fohlenfarbe(
            form_data["ex_vater"],     form_data["ex_mutter"],
            form_data["ag_vater"],     form_data["ag_mutter"],
            form_data["dun_vater"],    form_data["dun_mutter"],
            form_data["cr_vater"],     form_data["cr_mutter"],
            form_data["ch_vater"],     form_data["ch_mutter"],
            form_data["g_vater"],      form_data["g_mutter"],
            form_data["kit_vater"],    form_data["kit_mutter"],
            form_data["z_vater"],      form_data["z_mutter"],
            form_data["o_vater"],      form_data["o_mutter"],
            form_data["spl_vater"],    form_data["spl_mutter"],
            form_data["lp_vater"],     form_data["lp_mutter"],
            form_data["patn1_vater"],  form_data["patn1_mutter"]
        )

    return render_template(
        "index.html",
        gene_options_vater=gene_options_vater,
        gene_options_mutter=gene_options_mutter,
        results=results,
        form_data=form_data,
        default_values=default_values
    )
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
