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
        {'position': 1, 'entropy': 0.9999623941130954, 'variants_flattened': ['SKGKRTVDL', 'FHWLMLNPN'], 'supports': 2,
         'variants': [{'position': 1, 'sequence': 'SKGKRTVDL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 1, 'sequence': 'FHWLMLNPN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['FHWLMLNPN']}},
        {'position': 2, 'entropy': 0.9998683525288972, 'variants_flattened': ['KGKRTVDLG', 'HWLMLNPND'], 'supports': 2,
         'variants': [{'position': 2, 'sequence': 'KGKRTVDLG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 2, 'sequence': 'HWLMLNPND', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['HWLMLNPND']}},
        {'position': 3, 'entropy': 1.0000079547322183, 'variants_flattened': ['GKRTVDLGQ', 'WLMLNPNDT'], 'supports': 2,
         'variants': [{'position': 3, 'sequence': 'GKRTVDLGQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 3, 'sequence': 'WLMLNPNDT', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['WLMLNPNDT']}},
        {'position': 4, 'entropy': 1.0003357804798798, 'variants_flattened': ['KRTVDLGQC', 'LMLNPNDTV'], 'supports': 2,
         'variants': [{'position': 4, 'sequence': 'KRTVDLGQC', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 4, 'sequence': 'LMLNPNDTV', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['LMLNPNDTV']}},
        {'position': 5, 'entropy': 0.999952609077124, 'variants_flattened': ['RTVDLGQCG', 'MLNPNDTVT'], 'supports': 2,
         'variants': [{'position': 5, 'sequence': 'RTVDLGQCG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 5, 'sequence': 'MLNPNDTVT', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['MLNPNDTVT']}},
        {'position': 6, 'entropy': 0.9998514882055571, 'variants_flattened': ['TVDLGQCGL', 'LNPNDTVTF'], 'supports': 2,
         'variants': [{'position': 6, 'sequence': 'TVDLGQCGL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 6, 'sequence': 'LNPNDTVTF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['LNPNDTVTF']}},
        {'position': 7, 'entropy': 0.9999407922962504, 'variants_flattened': ['VDLGQCGLL', 'NPNDTVTFS'], 'supports': 2,
         'variants': [{'position': 7, 'sequence': 'VDLGQCGLL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 7, 'sequence': 'NPNDTVTFS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['NPNDTVTFS']}},
        {'position': 8, 'entropy': 0.9999184766521003, 'variants_flattened': ['DLGQCGLLG', 'PNDTVTFSF'], 'supports': 2,
         'variants': [{'position': 8, 'sequence': 'DLGQCGLLG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 8, 'sequence': 'PNDTVTFSF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['PNDTVTFSF']}},
        {'position': 9, 'entropy': 0.9998908146972026, 'variants_flattened': ['LGQCGLLGT', 'NDTVTFSFN'], 'supports': 2,
         'variants': [{'position': 9, 'sequence': 'LGQCGLLGT', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 9, 'sequence': 'NDTVTFSFN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['NDTVTFSFN']}},
        {'position': 10, 'entropy': 0.9997866473144991, 'variants_flattened': ['GQCGLLGTI', 'DTVTFSFNG'], 'supports': 2,
         'variants': [{'position': 10, 'sequence': 'GQCGLLGTI', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 10, 'sequence': 'DTVTFSFNG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['DTVTFSFNG']}},
        {'position': 11, 'entropy': 0.9997810718223481, 'variants_flattened': ['QCGLLGTIT', 'TVTFSFNGA'], 'supports': 2,
         'variants': [{'position': 11, 'sequence': 'QCGLLGTIT', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 11, 'sequence': 'TVTFSFNGA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['TVTFSFNGA']}},
        {'position': 12, 'entropy': 0.9999343493092119, 'variants_flattened': ['CGLLGTITG', 'VTFSFNGAF'], 'supports': 2,
         'variants': [{'position': 12, 'sequence': 'CGLLGTITG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 12, 'sequence': 'VTFSFNGAF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['VTFSFNGAF']}},
        {'position': 13, 'entropy': 0.9999972847510881, 'variants_flattened': ['GLLGTITGP', 'TFSFNGAFI'], 'supports': 2,
         'variants': [{'position': 13, 'sequence': 'GLLGTITGP', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 13, 'sequence': 'TFSFNGAFI', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['TFSFNGAFI']}},
        {'position': 14, 'entropy': 1.0000805058215247, 'variants_flattened': ['LLGTITGPP', 'FSFNGAFIA'], 'supports': 2,
         'variants': [{'position': 14, 'sequence': 'LLGTITGPP', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 14, 'sequence': 'FSFNGAFIA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['FSFNGAFIA']}},
        {'position': 15, 'entropy': 0.9998348190289994, 'variants_flattened': ['LGTITGPPQ', 'SFNGAFIAP'], 'supports': 2,
         'variants': [{'position': 15, 'sequence': 'LGTITGPPQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 15, 'sequence': 'SFNGAFIAP', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['SFNGAFIAP']}},
        {'position': 16, 'entropy': 1.0000762120791613, 'variants_flattened': ['GTITGPPQC', 'FNGAFIAPD'], 'supports': 2,
         'variants': [{'position': 16, 'sequence': 'GTITGPPQC', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 16, 'sequence': 'FNGAFIAPD', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['FNGAFIAPD']}},
        {'position': 17, 'entropy': 1.0000970851489488, 'variants_flattened': ['TITGPPQCD', 'NGAFIAPDR'], 'supports': 2,
         'variants': [{'position': 17, 'sequence': 'TITGPPQCD', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 17, 'sequence': 'NGAFIAPDR', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['NGAFIAPDR']}},
        {'position': 18, 'entropy': 0.9997396466188687, 'variants_flattened': ['ITGPPQCDQ', 'GAFIAPDRA'], 'supports': 2,
         'variants': [{'position': 18, 'sequence': 'ITGPPQCDQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 18, 'sequence': 'GAFIAPDRA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['GAFIAPDRA']}},
        {'position': 19, 'entropy': 0.9998666389130227, 'variants_flattened': ['TGPPQCDQF', 'AFIAPDRAS'], 'supports': 2,
         'variants': [{'position': 19, 'sequence': 'TGPPQCDQF', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 19, 'sequence': 'AFIAPDRAS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['AFIAPDRAS']}},
        {'position': 20, 'entropy': 0.9998277201572049, 'variants_flattened': ['GPPQCDQFL', 'FIAPDRASF'], 'supports': 2,
         'variants': [{'position': 20, 'sequence': 'GPPQCDQFL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 20, 'sequence': 'FIAPDRASF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['FIAPDRASF']}},
        {'position': 21, 'entropy': 1.0000124534615045, 'variants_flattened': ['PPQCDQFLE', 'IAPDRASFL'], 'supports': 2,
         'variants': [{'position': 21, 'sequence': 'PPQCDQFLE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 21, 'sequence': 'IAPDRASFL', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['IAPDRASFL']}},
        {'position': 22, 'entropy': 0.9999989058090761, 'variants_flattened': ['PQCDQFLEF', 'APDRASFLR'], 'supports': 2,
         'variants': [{'position': 22, 'sequence': 'PQCDQFLEF', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 22, 'sequence': 'APDRASFLR', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['APDRASFLR']}},
        {'position': 23, 'entropy': 0.9998705692072754, 'variants_flattened': ['QCDQFLEFS', 'PDRASFLRG'], 'supports': 2,
         'variants': [{'position': 23, 'sequence': 'QCDQFLEFS', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 23, 'sequence': 'PDRASFLRG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['PDRASFLRG']}},
        {'position': 24, 'entropy': 1.0001287202164346, 'variants_flattened': ['CDQFLEFSA', 'DRASFLRGK'], 'supports': 2,
         'variants': [{'position': 24, 'sequence': 'CDQFLEFSA', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 24, 'sequence': 'DRASFLRGK', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['DRASFLRGK']}},
        {'position': 25, 'entropy': 0.9997212771611049, 'variants_flattened': ['DQFLEFSAD', 'RASFLRGKS'], 'supports': 2,
         'variants': [{'position': 25, 'sequence': 'DQFLEFSAD', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 25, 'sequence': 'RASFLRGKS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['RASFLRGKS']}},
        {'position': 26, 'entropy': 1.0000668521237337, 'variants_flattened': ['QFLEFSADL', 'ASFLRGKSM'], 'supports': 2,
         'variants': [{'position': 26, 'sequence': 'QFLEFSADL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 26, 'sequence': 'ASFLRGKSM', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['ASFLRGKSM']}},
        {'position': 27, 'entropy': 0.9999882685647216, 'variants_flattened': ['FLEFSADLI', 'SFLRGKSMG'], 'supports': 2,
         'variants': [{'position': 27, 'sequence': 'FLEFSADLI', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 27, 'sequence': 'SFLRGKSMG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['SFLRGKSMG']}},
        {'position': 28, 'entropy': 0.9999435754011797, 'variants_flattened': ['LEFSADLII', 'FLRGKSMGI'], 'supports': 2,
         'variants': [{'position': 28, 'sequence': 'LEFSADLII', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 28, 'sequence': 'FLRGKSMGI', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['FLRGKSMGI']}},
        {'position': 29, 'entropy': 0.9997955164651995, 'variants_flattened': ['EFSADLIIE', 'LRGKSMGIQ'], 'supports': 2,
         'variants': [{'position': 29, 'sequence': 'EFSADLIIE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 29, 'sequence': 'LRGKSMGIQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['LRGKSMGIQ']}},
        {'position': 30, 'entropy': 0.9995638280725477, 'variants_flattened': ['FSADLIIER', 'RGKSMGIQS'], 'supports': 2,
         'variants': [{'position': 30, 'sequence': 'FSADLIIER', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 30, 'sequence': 'RGKSMGIQS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['RGKSMGIQS']}},
        {'position': 31, 'entropy': 1.0001046035295351, 'variants_flattened': ['SADLIIERR', 'GKSMGIQSG'], 'supports': 2,
         'variants': [{'position': 31, 'sequence': 'SADLIIERR', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 31, 'sequence': 'GKSMGIQSG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['GKSMGIQSG']}},
        {'position': 32, 'entropy': 1.000222735903312, 'variants_flattened': ['ADLIIERRE', 'KSMGIQSGV'], 'supports': 2,
         'variants': [{'position': 32, 'sequence': 'ADLIIERRE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 32, 'sequence': 'KSMGIQSGV', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['KSMGIQSGV']}},
        {'position': 33, 'entropy': 0.9999196059515298, 'variants_flattened': ['DLIIERREG', 'SMGIQSGVQ'], 'supports': 2,
         'variants': [{'position': 33, 'sequence': 'DLIIERREG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 33, 'sequence': 'SMGIQSGVQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['SMGIQSGVQ']}},
        {'position': 34, 'entropy': 1.0004411865496485, 'variants_flattened': ['LIIERREGS', 'MGIQSGVQV'], 'supports': 2,
         'variants': [{'position': 34, 'sequence': 'LIIERREGS', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 34, 'sequence': 'MGIQSGVQV', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['MGIQSGVQV']}},
        {'position': 35, 'entropy': 0.9999884554120021, 'variants_flattened': ['IIERREGSD', 'GIQSGVQVD'], 'supports': 2,
         'variants': [{'position': 35, 'sequence': 'IIERREGSD', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 35, 'sequence': 'GIQSGVQVD', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['GIQSGVQVD']}},
        {'position': 36, 'entropy': 1.0000393983103975, 'variants_flattened': ['IERREGSDV', 'IQSGVQVDA'], 'supports': 2,
         'variants': [{'position': 36, 'sequence': 'IERREGSDV', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 36, 'sequence': 'IQSGVQVDA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['IQSGVQVDA']}},
        {'position': 37, 'entropy': 1.0000161980712239, 'variants_flattened': ['ERREGSDVC', 'QSGVQVDAN'], 'supports': 2,
         'variants': [{'position': 37, 'sequence': 'ERREGSDVC', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 37, 'sequence': 'QSGVQVDAN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['QSGVQVDAN']}},
        {'position': 38, 'entropy': 0.9999330708631782, 'variants_flattened': ['RREGSDVCY', 'SGVQVDANC'], 'supports': 2,
         'variants': [{'position': 38, 'sequence': 'RREGSDVCY', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 38, 'sequence': 'SGVQVDANC', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['SGVQVDANC']}},
        {'position': 39, 'entropy': 1.000058271956235, 'variants_flattened': ['REGSDVCYP', 'GVQVDANCE'], 'supports': 2,
         'variants': [{'position': 39, 'sequence': 'REGSDVCYP', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 39, 'sequence': 'GVQVDANCE', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['GVQVDANCE']}},
        {'position': 40, 'entropy': 0.9998389744998988, 'variants_flattened': ['EGSDVCYPG', 'VQVDANCEG'], 'supports': 2,
         'variants': [{'position': 40, 'sequence': 'EGSDVCYPG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 40, 'sequence': 'VQVDANCEG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['VQVDANCEG']}},
        {'position': 41, 'entropy': 1.0001085108763246, 'variants_flattened': ['GSDVCYPGK', 'QVDANCEGD'], 'supports': 2,
         'variants': [{'position': 41, 'sequence': 'GSDVCYPGK', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 41, 'sequence': 'QVDANCEGD', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['QVDANCEGD']}},
        {'position': 42, 'entropy': 0.9999139223441444, 'variants_flattened': ['SDVCYPGKF', 'VDANCEGDC'], 'supports': 2,
         'variants': [{'position': 42, 'sequence': 'SDVCYPGKF', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 42, 'sequence': 'VDANCEGDC', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['VDANCEGDC']}},
        {'position': 43, 'entropy': 0.9999181156599856, 'variants_flattened': ['DVCYPGKFV', 'DANCEGDCY'], 'supports': 2,
         'variants': [{'position': 43, 'sequence': 'DVCYPGKFV', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 43, 'sequence': 'DANCEGDCY', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['DANCEGDCY']}},
        {'position': 44, 'entropy': 0.9997916434165673, 'variants_flattened': ['VCYPGKFVN', 'ANCEGDCYH'], 'supports': 2,
         'variants': [{'position': 44, 'sequence': 'VCYPGKFVN', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 44, 'sequence': 'ANCEGDCYH', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['ANCEGDCYH']}},
        {'position': 45, 'entropy': 0.9998806263784773, 'variants_flattened': ['CYPGKFVNE', 'NCEGDCYHS'], 'supports': 2,
         'variants': [{'position': 45, 'sequence': 'CYPGKFVNE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 45, 'sequence': 'NCEGDCYHS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['NCEGDCYHS']}},
        {'position': 46, 'entropy': 0.999970696793102, 'variants_flattened': ['YPGKFVNEE', 'CEGDCYHSG'], 'supports': 2,
         'variants': [{'position': 46, 'sequence': 'YPGKFVNEE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 46, 'sequence': 'CEGDCYHSG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['CEGDCYHSG']}},
        {'position': 47, 'entropy': 0.9998874671926381, 'variants_flattened': ['PGKFVNEEA', 'EGDCYHSGG'], 'supports': 2,
         'variants': [{'position': 47, 'sequence': 'PGKFVNEEA', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 47, 'sequence': 'EGDCYHSGG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['EGDCYHSGG']}},
        {'position': 48, 'entropy': 0.9999185240103808, 'variants_flattened': ['GKFVNEEAL', 'GDCYHSGGT'], 'supports': 2,
         'variants': [{'position': 48, 'sequence': 'GKFVNEEAL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 48, 'sequence': 'GDCYHSGGT', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['GDCYHSGGT']}},
        {'position': 49, 'entropy': 0.9994179784233967, 'variants_flattened': ['KFVNEEALR', 'DCYHSGGTI'], 'supports': 2,
         'variants': [{'position': 49, 'sequence': 'KFVNEEALR', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 49, 'sequence': 'DCYHSGGTI', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['DCYHSGGTI']}},
        {'position': 50, 'entropy': 1.0002079035265126, 'variants_flattened': ['FVNEEALRQ', 'CYHSGGTII'], 'supports': 2,
         'variants': [{'position': 50, 'sequence': 'FVNEEALRQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 50, 'sequence': 'CYHSGGTII', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['CYHSGGTII']}},
        {'position': 51, 'entropy': 0.9999603646828494, 'variants_flattened': ['VNEEALRQI', 'YHSGGTIIS'], 'supports': 2,
         'variants': [{'position': 51, 'sequence': 'VNEEALRQI', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 51, 'sequence': 'YHSGGTIIS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['YHSGGTIIS']}},
        {'position': 52, 'entropy': 0.9999766002262573, 'variants_flattened': ['NEEALRQIL', 'HSGGTIISN'], 'supports': 2,
         'variants': [{'position': 52, 'sequence': 'NEEALRQIL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                       'motif_long': 'Index'},
                      {'position': 52, 'sequence': 'HSGGTIISN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                       'motif_long': 'Major'}], 'kmer_types': {'incidence': 50.0, 'types': ['HSGGTIISN']}}]


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
