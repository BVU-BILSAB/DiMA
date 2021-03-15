import pytest
from io import StringIO
import subprocess
from json import loads

@pytest.fixture
def test_input_data():
    return """>Seq_1
SKGKRTVDLGQCGLLGTITGPPQCDQFLEFSADLIIERREGSDVCYPGKFVNEEALRQIL
>Seq_2
FHWLMLNPNDTVTFSFNGAFIAPDRASFLRGKSMGIQSGVQVDANCEGDCYHSGGTIISN"""


@pytest.fixture
def test_output_data():
    return [{'position': 1, 'entropy': 0.9996941527863118, 'variants_flattened': ['SKGKRTVDL', 'FHWLMLNPN'],
             'supports': 2, 'variants': [
            {'position': 1, 'sequence': 'SKGKRTVDL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
             'motif_long': 'Index'},
            {'position': 1, 'sequence': 'FHWLMLNPN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
             'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['SKGKRTVDL', 'FHWLMLNPN']},
            {'position': 2, 'entropy': 0.9998527825248205, 'variants_flattened': ['KGKRTVDLG', 'HWLMLNPND'],
             'supports': 2, 'variants': [
                {'position': 2, 'sequence': 'KGKRTVDLG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 2, 'sequence': 'HWLMLNPND', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['KGKRTVDLG', 'HWLMLNPND']},
            {'position': 3, 'entropy': 1.0002077903270306, 'variants_flattened': ['GKRTVDLGQ', 'WLMLNPNDT'],
             'supports': 2, 'variants': [
                {'position': 3, 'sequence': 'GKRTVDLGQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 3, 'sequence': 'WLMLNPNDT', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['GKRTVDLGQ', 'WLMLNPNDT']},
            {'position': 4, 'entropy': 0.9998767156387527, 'variants_flattened': ['KRTVDLGQC', 'LMLNPNDTV'],
             'supports': 2, 'variants': [
                {'position': 4, 'sequence': 'KRTVDLGQC', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 4, 'sequence': 'LMLNPNDTV', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['KRTVDLGQC', 'LMLNPNDTV']},
            {'position': 5, 'entropy': 0.9999990907616566, 'variants_flattened': ['RTVDLGQCG', 'MLNPNDTVT'],
             'supports': 2, 'variants': [
                {'position': 5, 'sequence': 'RTVDLGQCG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 5, 'sequence': 'MLNPNDTVT', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['RTVDLGQCG', 'MLNPNDTVT']},
            {'position': 6, 'entropy': 0.9997319913436709, 'variants_flattened': ['TVDLGQCGL', 'LNPNDTVTF'],
             'supports': 2, 'variants': [
                {'position': 6, 'sequence': 'TVDLGQCGL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 6, 'sequence': 'LNPNDTVTF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['TVDLGQCGL', 'LNPNDTVTF']},
            {'position': 7, 'entropy': 0.9999358611228004, 'variants_flattened': ['VDLGQCGLL', 'NPNDTVTFS'],
             'supports': 2, 'variants': [
                {'position': 7, 'sequence': 'VDLGQCGLL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 7, 'sequence': 'NPNDTVTFS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['VDLGQCGLL', 'NPNDTVTFS']},
            {'position': 8, 'entropy': 0.9996401848416852, 'variants_flattened': ['DLGQCGLLG', 'PNDTVTFSF'],
             'supports': 2, 'variants': [
                {'position': 8, 'sequence': 'DLGQCGLLG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 8, 'sequence': 'PNDTVTFSF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['DLGQCGLLG', 'PNDTVTFSF']},
            {'position': 9, 'entropy': 0.999835010171886, 'variants_flattened': ['LGQCGLLGT', 'NDTVTFSFN'],
             'supports': 2, 'variants': [
                {'position': 9, 'sequence': 'LGQCGLLGT', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 9, 'sequence': 'NDTVTFSFN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['LGQCGLLGT', 'NDTVTFSFN']},
            {'position': 10, 'entropy': 1.0000285206003887, 'variants_flattened': ['GQCGLLGTI', 'DTVTFSFNG'],
             'supports': 2, 'variants': [
                {'position': 10, 'sequence': 'GQCGLLGTI', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 10, 'sequence': 'DTVTFSFNG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['GQCGLLGTI', 'DTVTFSFNG']},
            {'position': 11, 'entropy': 0.9998620280532521, 'variants_flattened': ['QCGLLGTIT', 'TVTFSFNGA'],
             'supports': 2, 'variants': [
                {'position': 11, 'sequence': 'QCGLLGTIT', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 11, 'sequence': 'TVTFSFNGA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['QCGLLGTIT', 'TVTFSFNGA']},
            {'position': 12, 'entropy': 1.000727302164749, 'variants_flattened': ['CGLLGTITG', 'VTFSFNGAF'],
             'supports': 2, 'variants': [
                {'position': 12, 'sequence': 'CGLLGTITG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 12, 'sequence': 'VTFSFNGAF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['CGLLGTITG', 'VTFSFNGAF']},
            {'position': 13, 'entropy': 1.0001649797128818, 'variants_flattened': ['GLLGTITGP', 'TFSFNGAFI'],
             'supports': 2, 'variants': [
                {'position': 13, 'sequence': 'GLLGTITGP', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 13, 'sequence': 'TFSFNGAFI', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['GLLGTITGP', 'TFSFNGAFI']},
            {'position': 14, 'entropy': 0.9998262612423817, 'variants_flattened': ['LLGTITGPP', 'FSFNGAFIA'],
             'supports': 2, 'variants': [
                {'position': 14, 'sequence': 'LLGTITGPP', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 14, 'sequence': 'FSFNGAFIA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['LLGTITGPP', 'FSFNGAFIA']},
            {'position': 15, 'entropy': 0.9999833931390844, 'variants_flattened': ['LGTITGPPQ', 'SFNGAFIAP'],
             'supports': 2, 'variants': [
                {'position': 15, 'sequence': 'LGTITGPPQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 15, 'sequence': 'SFNGAFIAP', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['LGTITGPPQ', 'SFNGAFIAP']},
            {'position': 16, 'entropy': 0.9998775907283515, 'variants_flattened': ['GTITGPPQC', 'FNGAFIAPD'],
             'supports': 2, 'variants': [
                {'position': 16, 'sequence': 'GTITGPPQC', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 16, 'sequence': 'FNGAFIAPD', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['GTITGPPQC', 'FNGAFIAPD']},
            {'position': 17, 'entropy': 1.0003152583118762, 'variants_flattened': ['TITGPPQCD', 'NGAFIAPDR'],
             'supports': 2, 'variants': [
                {'position': 17, 'sequence': 'TITGPPQCD', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 17, 'sequence': 'NGAFIAPDR', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['TITGPPQCD', 'NGAFIAPDR']},
            {'position': 18, 'entropy': 0.9999186441494927, 'variants_flattened': ['ITGPPQCDQ', 'GAFIAPDRA'],
             'supports': 2, 'variants': [
                {'position': 18, 'sequence': 'ITGPPQCDQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 18, 'sequence': 'GAFIAPDRA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['ITGPPQCDQ', 'GAFIAPDRA']},
            {'position': 19, 'entropy': 1.0001076904486752, 'variants_flattened': ['TGPPQCDQF', 'AFIAPDRAS'],
             'supports': 2, 'variants': [
                {'position': 19, 'sequence': 'TGPPQCDQF', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 19, 'sequence': 'AFIAPDRAS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['TGPPQCDQF', 'AFIAPDRAS']},
            {'position': 20, 'entropy': 0.9998902777404496, 'variants_flattened': ['GPPQCDQFL', 'FIAPDRASF'],
             'supports': 2, 'variants': [
                {'position': 20, 'sequence': 'GPPQCDQFL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 20, 'sequence': 'FIAPDRASF', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['GPPQCDQFL', 'FIAPDRASF']},
            {'position': 21, 'entropy': 0.9998907985361742, 'variants_flattened': ['PPQCDQFLE', 'IAPDRASFL'],
             'supports': 2, 'variants': [
                {'position': 21, 'sequence': 'PPQCDQFLE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 21, 'sequence': 'IAPDRASFL', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['PPQCDQFLE', 'IAPDRASFL']},
            {'position': 22, 'entropy': 0.9998114932678888, 'variants_flattened': ['PQCDQFLEF', 'APDRASFLR'],
             'supports': 2, 'variants': [
                {'position': 22, 'sequence': 'PQCDQFLEF', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 22, 'sequence': 'APDRASFLR', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['PQCDQFLEF', 'APDRASFLR']},
            {'position': 23, 'entropy': 1.0000842022999432, 'variants_flattened': ['QCDQFLEFS', 'PDRASFLRG'],
             'supports': 2, 'variants': [
                {'position': 23, 'sequence': 'QCDQFLEFS', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 23, 'sequence': 'PDRASFLRG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['QCDQFLEFS', 'PDRASFLRG']},
            {'position': 24, 'entropy': 1.000033942370331, 'variants_flattened': ['CDQFLEFSA', 'DRASFLRGK'],
             'supports': 2, 'variants': [
                {'position': 24, 'sequence': 'CDQFLEFSA', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 24, 'sequence': 'DRASFLRGK', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['CDQFLEFSA', 'DRASFLRGK']},
            {'position': 25, 'entropy': 1.0002065938605047, 'variants_flattened': ['DQFLEFSAD', 'RASFLRGKS'],
             'supports': 2, 'variants': [
                {'position': 25, 'sequence': 'DQFLEFSAD', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 25, 'sequence': 'RASFLRGKS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['DQFLEFSAD', 'RASFLRGKS']},
            {'position': 26, 'entropy': 0.9999082272003921, 'variants_flattened': ['QFLEFSADL', 'ASFLRGKSM'],
             'supports': 2, 'variants': [
                {'position': 26, 'sequence': 'QFLEFSADL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 26, 'sequence': 'ASFLRGKSM', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['QFLEFSADL', 'ASFLRGKSM']},
            {'position': 27, 'entropy': 0.999922974469553, 'variants_flattened': ['FLEFSADLI', 'SFLRGKSMG'],
             'supports': 2, 'variants': [
                {'position': 27, 'sequence': 'FLEFSADLI', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 27, 'sequence': 'SFLRGKSMG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['FLEFSADLI', 'SFLRGKSMG']},
            {'position': 28, 'entropy': 0.9998630432180257, 'variants_flattened': ['LEFSADLII', 'FLRGKSMGI'],
             'supports': 2, 'variants': [
                {'position': 28, 'sequence': 'LEFSADLII', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 28, 'sequence': 'FLRGKSMGI', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['LEFSADLII', 'FLRGKSMGI']},
            {'position': 29, 'entropy': 0.9999530653393308, 'variants_flattened': ['EFSADLIIE', 'LRGKSMGIQ'],
             'supports': 2, 'variants': [
                {'position': 29, 'sequence': 'EFSADLIIE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 29, 'sequence': 'LRGKSMGIQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['EFSADLIIE', 'LRGKSMGIQ']},
            {'position': 30, 'entropy': 0.999824893735689, 'variants_flattened': ['FSADLIIER', 'RGKSMGIQS'],
             'supports': 2, 'variants': [
                {'position': 30, 'sequence': 'FSADLIIER', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 30, 'sequence': 'RGKSMGIQS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['FSADLIIER', 'RGKSMGIQS']},
            {'position': 31, 'entropy': 0.9999774670272372, 'variants_flattened': ['SADLIIERR', 'GKSMGIQSG'],
             'supports': 2, 'variants': [
                {'position': 31, 'sequence': 'SADLIIERR', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 31, 'sequence': 'GKSMGIQSG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['SADLIIERR', 'GKSMGIQSG']},
            {'position': 32, 'entropy': 0.9999315202417236, 'variants_flattened': ['ADLIIERRE', 'KSMGIQSGV'],
             'supports': 2, 'variants': [
                {'position': 32, 'sequence': 'ADLIIERRE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 32, 'sequence': 'KSMGIQSGV', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['ADLIIERRE', 'KSMGIQSGV']},
            {'position': 33, 'entropy': 0.9997854784050849, 'variants_flattened': ['DLIIERREG', 'SMGIQSGVQ'],
             'supports': 2, 'variants': [
                {'position': 33, 'sequence': 'DLIIERREG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 33, 'sequence': 'SMGIQSGVQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['DLIIERREG', 'SMGIQSGVQ']},
            {'position': 34, 'entropy': 0.9999510804117443, 'variants_flattened': ['LIIERREGS', 'MGIQSGVQV'],
             'supports': 2, 'variants': [
                {'position': 34, 'sequence': 'LIIERREGS', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 34, 'sequence': 'MGIQSGVQV', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['LIIERREGS', 'MGIQSGVQV']},
            {'position': 35, 'entropy': 1.0003439012484006, 'variants_flattened': ['IIERREGSD', 'GIQSGVQVD'],
             'supports': 2, 'variants': [
                {'position': 35, 'sequence': 'IIERREGSD', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 35, 'sequence': 'GIQSGVQVD', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['IIERREGSD', 'GIQSGVQVD']},
            {'position': 36, 'entropy': 0.9998285353136707, 'variants_flattened': ['IERREGSDV', 'IQSGVQVDA'],
             'supports': 2, 'variants': [
                {'position': 36, 'sequence': 'IERREGSDV', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 36, 'sequence': 'IQSGVQVDA', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['IERREGSDV', 'IQSGVQVDA']},
            {'position': 37, 'entropy': 0.9998773652600927, 'variants_flattened': ['ERREGSDVC', 'QSGVQVDAN'],
             'supports': 2, 'variants': [
                {'position': 37, 'sequence': 'ERREGSDVC', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 37, 'sequence': 'QSGVQVDAN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['ERREGSDVC', 'QSGVQVDAN']},
            {'position': 38, 'entropy': 0.9999179710107026, 'variants_flattened': ['RREGSDVCY', 'SGVQVDANC'],
             'supports': 2, 'variants': [
                {'position': 38, 'sequence': 'RREGSDVCY', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 38, 'sequence': 'SGVQVDANC', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['RREGSDVCY', 'SGVQVDANC']},
            {'position': 39, 'entropy': 1.0000709306712021, 'variants_flattened': ['REGSDVCYP', 'GVQVDANCE'],
             'supports': 2, 'variants': [
                {'position': 39, 'sequence': 'REGSDVCYP', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 39, 'sequence': 'GVQVDANCE', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['REGSDVCYP', 'GVQVDANCE']},
            {'position': 40, 'entropy': 1.00022708390481, 'variants_flattened': ['EGSDVCYPG', 'VQVDANCEG'],
             'supports': 2, 'variants': [
                {'position': 40, 'sequence': 'EGSDVCYPG', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 40, 'sequence': 'VQVDANCEG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['EGSDVCYPG', 'VQVDANCEG']},
            {'position': 41, 'entropy': 1.0000416729069816, 'variants_flattened': ['GSDVCYPGK', 'QVDANCEGD'],
             'supports': 2, 'variants': [
                {'position': 41, 'sequence': 'GSDVCYPGK', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 41, 'sequence': 'QVDANCEGD', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['GSDVCYPGK', 'QVDANCEGD']},
            {'position': 42, 'entropy': 0.9999078617169035, 'variants_flattened': ['SDVCYPGKF', 'VDANCEGDC'],
             'supports': 2, 'variants': [
                {'position': 42, 'sequence': 'SDVCYPGKF', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 42, 'sequence': 'VDANCEGDC', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['SDVCYPGKF', 'VDANCEGDC']},
            {'position': 43, 'entropy': 0.9999383011830356, 'variants_flattened': ['DVCYPGKFV', 'DANCEGDCY'],
             'supports': 2, 'variants': [
                {'position': 43, 'sequence': 'DVCYPGKFV', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 43, 'sequence': 'DANCEGDCY', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['DVCYPGKFV', 'DANCEGDCY']},
            {'position': 44, 'entropy': 0.9996468948305757, 'variants_flattened': ['VCYPGKFVN', 'ANCEGDCYH'],
             'supports': 2, 'variants': [
                {'position': 44, 'sequence': 'VCYPGKFVN', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 44, 'sequence': 'ANCEGDCYH', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['VCYPGKFVN', 'ANCEGDCYH']},
            {'position': 45, 'entropy': 0.9997048564780862, 'variants_flattened': ['CYPGKFVNE', 'NCEGDCYHS'],
             'supports': 2, 'variants': [
                {'position': 45, 'sequence': 'CYPGKFVNE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 45, 'sequence': 'NCEGDCYHS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['CYPGKFVNE', 'NCEGDCYHS']},
            {'position': 46, 'entropy': 0.9998877708918318, 'variants_flattened': ['YPGKFVNEE', 'CEGDCYHSG'],
             'supports': 2, 'variants': [
                {'position': 46, 'sequence': 'YPGKFVNEE', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 46, 'sequence': 'CEGDCYHSG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['YPGKFVNEE', 'CEGDCYHSG']},
            {'position': 47, 'entropy': 0.9999364789901649, 'variants_flattened': ['PGKFVNEEA', 'EGDCYHSGG'],
             'supports': 2, 'variants': [
                {'position': 47, 'sequence': 'PGKFVNEEA', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 47, 'sequence': 'EGDCYHSGG', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['PGKFVNEEA', 'EGDCYHSGG']},
            {'position': 48, 'entropy': 0.9997876599143143, 'variants_flattened': ['GKFVNEEAL', 'GDCYHSGGT'],
             'supports': 2, 'variants': [
                {'position': 48, 'sequence': 'GKFVNEEAL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 48, 'sequence': 'GDCYHSGGT', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['GKFVNEEAL', 'GDCYHSGGT']},
            {'position': 49, 'entropy': 0.9998724380712871, 'variants_flattened': ['KFVNEEALR', 'DCYHSGGTI'],
             'supports': 2, 'variants': [
                {'position': 49, 'sequence': 'KFVNEEALR', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 49, 'sequence': 'DCYHSGGTI', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['KFVNEEALR', 'DCYHSGGTI']},
            {'position': 50, 'entropy': 1.0000566686449757, 'variants_flattened': ['FVNEEALRQ', 'CYHSGGTII'],
             'supports': 2, 'variants': [
                {'position': 50, 'sequence': 'FVNEEALRQ', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 50, 'sequence': 'CYHSGGTII', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['FVNEEALRQ', 'CYHSGGTII']},
            {'position': 51, 'entropy': 1.0002763318060592, 'variants_flattened': ['VNEEALRQI', 'YHSGGTIIS'],
             'supports': 2, 'variants': [
                {'position': 51, 'sequence': 'VNEEALRQI', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 51, 'sequence': 'YHSGGTIIS', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['VNEEALRQI', 'YHSGGTIIS']},
            {'position': 52, 'entropy': 1.0002913393133699, 'variants_flattened': ['NEEALRQIL', 'HSGGTIISN'],
             'supports': 2, 'variants': [
                {'position': 52, 'sequence': 'NEEALRQIL', 'count': 1, 'incidence': 50.0, 'motif_short': 'I',
                 'motif_long': 'Index'},
                {'position': 52, 'sequence': 'HSGGTIISN', 'count': 1, 'incidence': 50.0, 'motif_short': 'Ma',
                 'motif_long': 'Major'}], 'variants': 2, 'kmer_types': ['NEEALRQIL', 'HSGGTIISN']}]


def test_run_module(test_input_data, test_output_data):
    from hunana import Hunana
    handle = StringIO(test_input_data)

    results = Hunana(handle).run()

    for results, test in zip(results, test_output_data):
        assert results.get('position') == test.get('position')
        assert results.get('supports') == test.get('supports')
        assert results.get('variants') == test.get('variants')
        assert results.get('kmer_types') == test.get('kmer_types')


def test_run_cli(test_input_data, test_output_data):
    process = subprocess.run(['hunana'], input=test_input_data.encode('utf-8'), shell=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert process.returncode == 0

    results = loads(process.stdout.decode('utf-8'))

    for results, test in zip(results, test_output_data):
        assert results.get('position') == test.get('position')
        assert results.get('supports') == test.get('supports')
        assert results.get('variants') == test.get('variants')
        assert results.get('kmer_types') == test.get('kmer_types')
