import pytest
from io import StringIO
import subprocess
from json import loads


@pytest.fixture
def test_input_data_basic():
    return """>Seq_1
SKGKRTVDLGQCGLLGTITGPPQCDQFLEFSADLIIERREGSDVCYPGKFVNEEALRQIL
>Seq_2
FHWLMLNPNDTVTFSFNGAFIAPDRASFLRGKSMGIQSGVQVDANCEGDCYHSGGTIISN"""


@pytest.fixture
def test_input_data_basic_unaligned():
    return """>Seq_1
SKGKRTVDLGQCGLLGTITGPPQCDQFLEFSADLIIERREGSDVCYPGKFVNEEALRQIL
>Seq_2
FHWLMLNPNDTVTFSFNGAFIAPDRASFLRGKSMGGIQSGVQVDANCEGDCYHSGGTIISN"""


@pytest.fixture
def test_output_data_basic():
    return [
        {'position': 1, 'entropy': 0.999961418135675, 'variants_flattened': ['SKGKRTVDL', 'FHWLMLNPN'], 'supports': 2,
         'variants': [{'position': 1, 'sequence': 'SKGKRTVDL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 1, 'sequence': 'FHWLMLNPN', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['SKGKRTVDL', 'FHWLMLNPN']}},
        {'position': 2, 'entropy': 1.000028099248692, 'variants_flattened': ['KGKRTVDLG', 'HWLMLNPND'], 'supports': 2,
         'variants': [{'position': 2, 'sequence': 'KGKRTVDLG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 2, 'sequence': 'HWLMLNPND', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['KGKRTVDLG', 'HWLMLNPND']}},
        {'position': 3, 'entropy': 0.9999584451899978, 'variants_flattened': ['GKRTVDLGQ', 'WLMLNPNDT'], 'supports': 2,
         'variants': [{'position': 3, 'sequence': 'GKRTVDLGQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 3, 'sequence': 'WLMLNPNDT', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['GKRTVDLGQ', 'WLMLNPNDT']}},
        {'position': 4, 'entropy': 0.9999328990325586, 'variants_flattened': ['KRTVDLGQC', 'LMLNPNDTV'], 'supports': 2,
         'variants': [{'position': 4, 'sequence': 'KRTVDLGQC', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 4, 'sequence': 'LMLNPNDTV', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['KRTVDLGQC', 'LMLNPNDTV']}},
        {'position': 5, 'entropy': 1.000246419381598, 'variants_flattened': ['RTVDLGQCG', 'MLNPNDTVT'], 'supports': 2,
         'variants': [{'position': 5, 'sequence': 'RTVDLGQCG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 5, 'sequence': 'MLNPNDTVT', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['RTVDLGQCG', 'MLNPNDTVT']}},
        {'position': 6, 'entropy': 0.999920482286929, 'variants_flattened': ['TVDLGQCGL', 'LNPNDTVTF'], 'supports': 2,
         'variants': [{'position': 6, 'sequence': 'TVDLGQCGL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 6, 'sequence': 'LNPNDTVTF', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['TVDLGQCGL', 'LNPNDTVTF']}},
        {'position': 7, 'entropy': 0.9999118599259772, 'variants_flattened': ['VDLGQCGLL', 'NPNDTVTFS'], 'supports': 2,
         'variants': [{'position': 7, 'sequence': 'VDLGQCGLL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 7, 'sequence': 'NPNDTVTFS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['VDLGQCGLL', 'NPNDTVTFS']}},
        {'position': 8, 'entropy': 0.9998189376838397, 'variants_flattened': ['DLGQCGLLG', 'PNDTVTFSF'], 'supports': 2,
         'variants': [{'position': 8, 'sequence': 'DLGQCGLLG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 8, 'sequence': 'PNDTVTFSF', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['DLGQCGLLG', 'PNDTVTFSF']}},
        {'position': 9, 'entropy': 0.9996939758276844, 'variants_flattened': ['LGQCGLLGT', 'NDTVTFSFN'], 'supports': 2,
         'variants': [{'position': 9, 'sequence': 'LGQCGLLGT', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 9, 'sequence': 'NDTVTFSFN', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['LGQCGLLGT', 'NDTVTFSFN']}},
        {'position': 10, 'entropy': 0.9998570267704489, 'variants_flattened': ['GQCGLLGTI', 'DTVTFSFNG'], 'supports': 2,
         'variants': [{'position': 10, 'sequence': 'GQCGLLGTI', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 10, 'sequence': 'DTVTFSFNG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['GQCGLLGTI', 'DTVTFSFNG']}},
        {'position': 11, 'entropy': 0.9999818949938919, 'variants_flattened': ['QCGLLGTIT', 'TVTFSFNGA'], 'supports': 2,
         'variants': [{'position': 11, 'sequence': 'QCGLLGTIT', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 11, 'sequence': 'TVTFSFNGA', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['QCGLLGTIT', 'TVTFSFNGA']}},
        {'position': 12, 'entropy': 1.0001775769494698, 'variants_flattened': ['CGLLGTITG', 'VTFSFNGAF'], 'supports': 2,
         'variants': [{'position': 12, 'sequence': 'CGLLGTITG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 12, 'sequence': 'VTFSFNGAF', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['CGLLGTITG', 'VTFSFNGAF']}},
        {'position': 13, 'entropy': 0.9998036204732288, 'variants_flattened': ['GLLGTITGP', 'TFSFNGAFI'], 'supports': 2,
         'variants': [{'position': 13, 'sequence': 'GLLGTITGP', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 13, 'sequence': 'TFSFNGAFI', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['GLLGTITGP', 'TFSFNGAFI']}},
        {'position': 14, 'entropy': 0.9999586760456964, 'variants_flattened': ['LLGTITGPP', 'FSFNGAFIA'], 'supports': 2,
         'variants': [{'position': 14, 'sequence': 'LLGTITGPP', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 14, 'sequence': 'FSFNGAFIA', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['LLGTITGPP', 'FSFNGAFIA']}},
        {'position': 15, 'entropy': 0.9997516470056456, 'variants_flattened': ['LGTITGPPQ', 'SFNGAFIAP'], 'supports': 2,
         'variants': [{'position': 15, 'sequence': 'LGTITGPPQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 15, 'sequence': 'SFNGAFIAP', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['LGTITGPPQ', 'SFNGAFIAP']}},
        {'position': 16, 'entropy': 1.000137282447823, 'variants_flattened': ['GTITGPPQC', 'FNGAFIAPD'], 'supports': 2,
         'variants': [{'position': 16, 'sequence': 'GTITGPPQC', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 16, 'sequence': 'FNGAFIAPD', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['GTITGPPQC', 'FNGAFIAPD']}},
        {'position': 17, 'entropy': 1.0000030351833937, 'variants_flattened': ['TITGPPQCD', 'NGAFIAPDR'], 'supports': 2,
         'variants': [{'position': 17, 'sequence': 'TITGPPQCD', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 17, 'sequence': 'NGAFIAPDR', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['TITGPPQCD', 'NGAFIAPDR']}},
        {'position': 18, 'entropy': 1.0003842245682963, 'variants_flattened': ['ITGPPQCDQ', 'GAFIAPDRA'], 'supports': 2,
         'variants': [{'position': 18, 'sequence': 'ITGPPQCDQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 18, 'sequence': 'GAFIAPDRA', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['ITGPPQCDQ', 'GAFIAPDRA']}},
        {'position': 19, 'entropy': 0.9998671158034738, 'variants_flattened': ['TGPPQCDQF', 'AFIAPDRAS'], 'supports': 2,
         'variants': [{'position': 19, 'sequence': 'TGPPQCDQF', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 19, 'sequence': 'AFIAPDRAS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['TGPPQCDQF', 'AFIAPDRAS']}},
        {'position': 20, 'entropy': 0.9999010488506052, 'variants_flattened': ['GPPQCDQFL', 'FIAPDRASF'], 'supports': 2,
         'variants': [{'position': 20, 'sequence': 'GPPQCDQFL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 20, 'sequence': 'FIAPDRASF', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['GPPQCDQFL', 'FIAPDRASF']}},
        {'position': 21, 'entropy': 0.9998731526465559, 'variants_flattened': ['PPQCDQFLE', 'IAPDRASFL'], 'supports': 2,
         'variants': [{'position': 21, 'sequence': 'PPQCDQFLE', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 21, 'sequence': 'IAPDRASFL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['PPQCDQFLE', 'IAPDRASFL']}},
        {'position': 22, 'entropy': 1.0000165661251388, 'variants_flattened': ['PQCDQFLEF', 'APDRASFLR'], 'supports': 2,
         'variants': [{'position': 22, 'sequence': 'PQCDQFLEF', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 22, 'sequence': 'APDRASFLR', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['PQCDQFLEF', 'APDRASFLR']}},
        {'position': 23, 'entropy': 1.0000360786790168, 'variants_flattened': ['QCDQFLEFS', 'PDRASFLRG'], 'supports': 2,
         'variants': [{'position': 23, 'sequence': 'QCDQFLEFS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 23, 'sequence': 'PDRASFLRG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['QCDQFLEFS', 'PDRASFLRG']}},
        {'position': 24, 'entropy': 0.9999881592256944, 'variants_flattened': ['CDQFLEFSA', 'DRASFLRGK'], 'supports': 2,
         'variants': [{'position': 24, 'sequence': 'CDQFLEFSA', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 24, 'sequence': 'DRASFLRGK', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['CDQFLEFSA', 'DRASFLRGK']}},
        {'position': 25, 'entropy': 1.0000312999352758, 'variants_flattened': ['DQFLEFSAD', 'RASFLRGKS'], 'supports': 2,
         'variants': [{'position': 25, 'sequence': 'DQFLEFSAD', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 25, 'sequence': 'RASFLRGKS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['DQFLEFSAD', 'RASFLRGKS']}},
        {'position': 26, 'entropy': 0.9998649986091327, 'variants_flattened': ['QFLEFSADL', 'ASFLRGKSM'], 'supports': 2,
         'variants': [{'position': 26, 'sequence': 'QFLEFSADL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 26, 'sequence': 'ASFLRGKSM', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['QFLEFSADL', 'ASFLRGKSM']}},
        {'position': 27, 'entropy': 1.0000020550633517, 'variants_flattened': ['FLEFSADLI', 'SFLRGKSMG'], 'supports': 2,
         'variants': [{'position': 27, 'sequence': 'FLEFSADLI', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 27, 'sequence': 'SFLRGKSMG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['FLEFSADLI', 'SFLRGKSMG']}},
        {'position': 28, 'entropy': 0.9999997622878796, 'variants_flattened': ['LEFSADLII', 'FLRGKSMGI'], 'supports': 2,
         'variants': [{'position': 28, 'sequence': 'LEFSADLII', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 28, 'sequence': 'FLRGKSMGI', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['LEFSADLII', 'FLRGKSMGI']}},
        {'position': 29, 'entropy': 1.0000438851156084, 'variants_flattened': ['EFSADLIIE', 'LRGKSMGIQ'], 'supports': 2,
         'variants': [{'position': 29, 'sequence': 'EFSADLIIE', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 29, 'sequence': 'LRGKSMGIQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['EFSADLIIE', 'LRGKSMGIQ']}},
        {'position': 30, 'entropy': 1.0000243404284104, 'variants_flattened': ['FSADLIIER', 'RGKSMGIQS'], 'supports': 2,
         'variants': [{'position': 30, 'sequence': 'FSADLIIER', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 30, 'sequence': 'RGKSMGIQS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['FSADLIIER', 'RGKSMGIQS']}},
        {'position': 31, 'entropy': 0.9998016966984364, 'variants_flattened': ['SADLIIERR', 'GKSMGIQSG'], 'supports': 2,
         'variants': [{'position': 31, 'sequence': 'SADLIIERR', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 31, 'sequence': 'GKSMGIQSG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['SADLIIERR', 'GKSMGIQSG']}},
        {'position': 32, 'entropy': 1.000027356700128, 'variants_flattened': ['ADLIIERRE', 'KSMGIQSGV'], 'supports': 2,
         'variants': [{'position': 32, 'sequence': 'ADLIIERRE', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 32, 'sequence': 'KSMGIQSGV', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['ADLIIERRE', 'KSMGIQSGV']}},
        {'position': 33, 'entropy': 0.999891477777618, 'variants_flattened': ['DLIIERREG', 'SMGIQSGVQ'], 'supports': 2,
         'variants': [{'position': 33, 'sequence': 'DLIIERREG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 33, 'sequence': 'SMGIQSGVQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['DLIIERREG', 'SMGIQSGVQ']}},
        {'position': 34, 'entropy': 0.9996563789567378, 'variants_flattened': ['LIIERREGS', 'MGIQSGVQV'], 'supports': 2,
         'variants': [{'position': 34, 'sequence': 'LIIERREGS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 34, 'sequence': 'MGIQSGVQV', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['LIIERREGS', 'MGIQSGVQV']}},
        {'position': 35, 'entropy': 1.0000402854660637, 'variants_flattened': ['IIERREGSD', 'GIQSGVQVD'], 'supports': 2,
         'variants': [{'position': 35, 'sequence': 'IIERREGSD', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 35, 'sequence': 'GIQSGVQVD', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['IIERREGSD', 'GIQSGVQVD']}},
        {'position': 36, 'entropy': 0.9999879346009815, 'variants_flattened': ['IERREGSDV', 'IQSGVQVDA'], 'supports': 2,
         'variants': [{'position': 36, 'sequence': 'IERREGSDV', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 36, 'sequence': 'IQSGVQVDA', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['IERREGSDV', 'IQSGVQVDA']}},
        {'position': 37, 'entropy': 0.9998820039560291, 'variants_flattened': ['ERREGSDVC', 'QSGVQVDAN'], 'supports': 2,
         'variants': [{'position': 37, 'sequence': 'ERREGSDVC', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 37, 'sequence': 'QSGVQVDAN', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['ERREGSDVC', 'QSGVQVDAN']}},
        {'position': 38, 'entropy': 1.000233962428959, 'variants_flattened': ['RREGSDVCY', 'SGVQVDANC'], 'supports': 2,
         'variants': [{'position': 38, 'sequence': 'RREGSDVCY', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 38, 'sequence': 'SGVQVDANC', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['RREGSDVCY', 'SGVQVDANC']}},
        {'position': 39, 'entropy': 1.0000110251126024, 'variants_flattened': ['REGSDVCYP', 'GVQVDANCE'], 'supports': 2,
         'variants': [{'position': 39, 'sequence': 'REGSDVCYP', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 39, 'sequence': 'GVQVDANCE', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['REGSDVCYP', 'GVQVDANCE']}},
        {'position': 40, 'entropy': 1.0001883473632185, 'variants_flattened': ['EGSDVCYPG', 'VQVDANCEG'], 'supports': 2,
         'variants': [{'position': 40, 'sequence': 'EGSDVCYPG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 40, 'sequence': 'VQVDANCEG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['EGSDVCYPG', 'VQVDANCEG']}},
        {'position': 41, 'entropy': 0.9999691745004053, 'variants_flattened': ['GSDVCYPGK', 'QVDANCEGD'], 'supports': 2,
         'variants': [{'position': 41, 'sequence': 'GSDVCYPGK', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 41, 'sequence': 'QVDANCEGD', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['GSDVCYPGK', 'QVDANCEGD']}},
        {'position': 42, 'entropy': 0.9999650658211922, 'variants_flattened': ['SDVCYPGKF', 'VDANCEGDC'], 'supports': 2,
         'variants': [{'position': 42, 'sequence': 'SDVCYPGKF', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 42, 'sequence': 'VDANCEGDC', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['SDVCYPGKF', 'VDANCEGDC']}},
        {'position': 43, 'entropy': 0.9998244472599646, 'variants_flattened': ['DVCYPGKFV', 'DANCEGDCY'], 'supports': 2,
         'variants': [{'position': 43, 'sequence': 'DVCYPGKFV', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 43, 'sequence': 'DANCEGDCY', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['DVCYPGKFV', 'DANCEGDCY']}},
        {'position': 44, 'entropy': 0.9999610488467693, 'variants_flattened': ['VCYPGKFVN', 'ANCEGDCYH'], 'supports': 2,
         'variants': [{'position': 44, 'sequence': 'VCYPGKFVN', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 44, 'sequence': 'ANCEGDCYH', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['VCYPGKFVN', 'ANCEGDCYH']}},
        {'position': 45, 'entropy': 1.0002040294503436, 'variants_flattened': ['CYPGKFVNE', 'NCEGDCYHS'], 'supports': 2,
         'variants': [{'position': 45, 'sequence': 'CYPGKFVNE', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 45, 'sequence': 'NCEGDCYHS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['CYPGKFVNE', 'NCEGDCYHS']}},
        {'position': 46, 'entropy': 1.001615765228175, 'variants_flattened': ['YPGKFVNEE', 'CEGDCYHSG'], 'supports': 2,
         'variants': [{'position': 46, 'sequence': 'YPGKFVNEE', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 46, 'sequence': 'CEGDCYHSG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['YPGKFVNEE', 'CEGDCYHSG']}},
        {'position': 47, 'entropy': 0.9997770863042704, 'variants_flattened': ['PGKFVNEEA', 'EGDCYHSGG'], 'supports': 2,
         'variants': [{'position': 47, 'sequence': 'PGKFVNEEA', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 47, 'sequence': 'EGDCYHSGG', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['PGKFVNEEA', 'EGDCYHSGG']}},
        {'position': 48, 'entropy': 0.999812546804468, 'variants_flattened': ['GKFVNEEAL', 'GDCYHSGGT'], 'supports': 2,
         'variants': [{'position': 48, 'sequence': 'GKFVNEEAL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 48, 'sequence': 'GDCYHSGGT', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['GKFVNEEAL', 'GDCYHSGGT']}},
        {'position': 49, 'entropy': 0.9995575449029701, 'variants_flattened': ['KFVNEEALR', 'DCYHSGGTI'], 'supports': 2,
         'variants': [{'position': 49, 'sequence': 'KFVNEEALR', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 49, 'sequence': 'DCYHSGGTI', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['KFVNEEALR', 'DCYHSGGTI']}},
        {'position': 50, 'entropy': 0.9997322513624165, 'variants_flattened': ['FVNEEALRQ', 'CYHSGGTII'], 'supports': 2,
         'variants': [{'position': 50, 'sequence': 'FVNEEALRQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 50, 'sequence': 'CYHSGGTII', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['FVNEEALRQ', 'CYHSGGTII']}},
        {'position': 51, 'entropy': 0.9998954419918495, 'variants_flattened': ['VNEEALRQI', 'YHSGGTIIS'], 'supports': 2,
         'variants': [{'position': 51, 'sequence': 'VNEEALRQI', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 51, 'sequence': 'YHSGGTIIS', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['VNEEALRQI', 'YHSGGTIIS']}},
        {'position': 52, 'entropy': 1.000084688018559, 'variants_flattened': ['NEEALRQIL', 'HSGGTIISN'], 'supports': 2,
         'variants': [{'position': 52, 'sequence': 'NEEALRQIL', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'},
                      {'position': 52, 'sequence': 'HSGGTIISN', 'count': 1, 'incidence': 50.0, 'motif_short': 'U',
                       'motif_long': 'Unique'}],
         'kmer_types': {'incidence': 50.0, 'types': ['NEEALRQIL', 'HSGGTIISN']}}]


def test_run_module_basic(test_input_data_basic, test_output_data_basic):
    from hunana import Hunana
    handle = StringIO(test_input_data_basic)

    results = Hunana(handle).run()

    for results, test in zip(results, test_output_data_basic):
        assert results.get('position') == test.get('position')
        assert results.get('supports') == test.get('supports')
        assert results.get('variants') == test.get('variants')
        assert results.get('kmer_types') == test.get('kmer_types')


def test_run_cli_basic(test_input_data_basic, test_output_data_basic):
    process = subprocess.run(['hunana'], input=test_input_data_basic.encode('utf-8'), shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    assert process.returncode == 0

    results = loads(process.stdout.decode('utf-8'))

    for results, test in zip(results, test_output_data_basic):
        assert results.get('position') == test.get('position')
        assert results.get('supports') == test.get('supports')
        assert results.get('variants') == test.get('variants')
        assert results.get('kmer_types') == test.get('kmer_types')


def test_run_module_basic_unaligned(test_input_data_basic_unaligned):
    from hunana import Hunana
    from hunana.errorhandlers.exceptions import SequenceLengthError

    handle = StringIO(test_input_data_basic_unaligned)

    with pytest.raises(SequenceLengthError):
        Hunana(handle).run()


def test_run_module_basic_kmer_len_invalid(test_input_data_basic):
    from hunana.errorhandlers.exceptions import InvalidKmerLength
    from hunana import Hunana

    handle = StringIO(test_input_data_basic)

    with pytest.raises(InvalidKmerLength):
        Hunana(handle, kmer_len=61).run()


def test_run_module_basic_no_seqs():
    from hunana.errorhandlers.exceptions import NoSequencesProvided
    from hunana import Hunana

    handle = StringIO('')

    with pytest.raises(NoSequencesProvided):
        Hunana(handle).run()
