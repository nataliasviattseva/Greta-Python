def si_len_matrices_egal(mat_a, mat_b):
    """Si la dimentions sont identiques"""
    if len(mat_a) == len(mat_b) and len(mat_a[0]) == len(mat_b[0]):
        return True
    else:
        return False


def addition(mat_a, mat_b):
    """Addition les deux matrices le même dimenton"""
    if si_len_matrices_egal(mat_a, mat_b):
        matrice_final = []
        for i in range(0, len(mat_a)):
            tmp = []
            for j in range(0, len(mat_a[i])):
                tmp.append(mat_a[i][j] + mat_b[i][j])
            matrice_final.append(tmp)
        return matrice_final
    else:
        return "Les dimention des matrices sont differents."


def multiplication_par_scalaire(mat, number):
    """Multiplication d'une matrice par un scalaire"""
    matrice_final = []
    for i in range(0, len(mat)):
        tmp = []
        for j in range(0, len(mat[i])):
            tmp.append(mat[i][j] * number)
        matrice_final.append(tmp)
    return matrice_final


def transition_matrice(mat):
    """Colonnes devient de lignes, lignes devient les colonnes"""
    trans_mat = []
    for i in range(len(mat[0])):
        tmp = []
        for j in range(len(mat)):
            tmp.append(mat[j][i])
        trans_mat.append(tmp)
    return trans_mat


def verifier_matrices_pour_multiplication(mat_a, mat_b):
    if len(mat_a[0]) == len(mat_b):
        return True
    else:
        return False


def multiplication_matrices(mat_a, mat_b):
    """Retourne la multiplication de matrices"""
    matrice_final = []
    if verifier_matrices_pour_multiplication(mat_a, mat_b):
        for i in range(0, len(mat_a)):
            tmp = []
            for j in range(0, len(mat_a[0])):
                total = 0
                for k in range(0, len(mat_a[0])):
                    total += mat_a[i][k]*mat_b[k][j]
                tmp.append(total)
            matrice_final.append(tmp)
        return matrice_final
    else:
        return "Ce n'est pas possible de multiplier les matrices"


def verifier_que_matrice_carre(matrice):
    if len(matrice) == len(matrice[0]) == 2:
        return True
    else:
        return False


def calcul_determinant_matrice_carre(matrice):
    if verifier_que_matrice_carre(matrice):
        determinant = matrice[0][0] * matrice[1][1] - matrice[1][0] * matrice[0][1]
    else:
        determinant = 0
    return determinant


def calcul_inversion_matrice_carre(matrice):
    det = calcul_determinant_matrice_carre(matrice)
    if det != 0:
        # Transposition de deux valeurs
        tmp = matrice[0][0]
        matrice[0][0] = matrice[1][1]
        matrice[1][1] = tmp

        matrice[0][1] *= -1
        matrice[1][0] *= -1

        mati = []
        for ligne in matrice:
            matj = []
            for element in ligne:
                matj.append(element * (1 / det))
            mati.append(matj)
        return mati
    else:
        print("Opération impossible. Le determinant est égale zero.")
        return None


def matrice_inversible(matrice):
    if calcul_determinant_matrice_carre(matrice) != 0:
        return True
    else:
        return False


def determiner_adjoint_matrice(matrice):
    if matrice_inversible(matrice):
        a = matrice[0][0]
        b = matrice[0][1]
        c = matrice[1][0]
        d = matrice[1][1]
        return [[d, (-1)*b], [(-1)*c, a]]
    else:
        return "pas ajustible"


def elimin_linelimin_lin_col_col(m, n, matrice_muneur):
    # Retourne la matrice matrice_mineur sans la m-ième ligne et la n-ième colonne
    matrice_mineur_lin = len(matrice_muneur)
    result = []
    rep = []
    for i in range(matrice_mineur_lin):
        if i != m:
            for j in range(matrice_mineur_lin):
                if j != n:
                    result.append(matrice_muneur[i][j])
    for k in range(0, len(result), matrice_mineur_lin - 1):
        rep.append(result[k:k + matrice_mineur_lin - 1])
    return rep
