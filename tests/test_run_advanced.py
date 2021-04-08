import pytest
from io import StringIO
import subprocess
from json import loads


@pytest.fixture
def test_input_data_advanced():
    return """>A|CY021716|A/AA/Huston/1945|USA
MERIKELRNLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPSLRMKWMMAMKYPITADKRITEMIPER

>A|CY020292|A/AA/Marton/1943|USA
NEQGQTLWSKMNDAGSDRVMVSPLAVTWWNRNGPMTSTVHYPKIYKTYFEKVERLKHGTFGPVHFRNQVK

>A|CY083917|A/Aalborg/INS132/2009|Denmark
MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMRYPITADKRIMDMIPER"""


@pytest.fixture
def test_input_data_advanced_missing_header_items():
    return """>A|CY021716|A/AA/Huston/1945|USA
MERIKELRNLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPSLRMKWMMAMKYPITADKRITEMIPER

>A|CY020292|A/AA/Marton/1943|
NEQGQTLWSKMNDAGSDRVMVSPLAVTWWNRNGPMTSTVHYPKIYKTYFEKVERLKHGTFGPVHFRNQVK

>A|CY083917|A/Aalborg/INS132/2009|Denmark
MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMRYPITADKRIMDMIPER"""


@pytest.fixture
def test_input_data_advanced_item_count_invalid():
    return """>A|CY021716|A/AA/Huston/1945|USA
MERIKELRNLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPSLRMKWMMAMKYPITADKRITEMIPER

>A|CY020292|A/AA/Marton/1943|USA
NEQGQTLWSKMNDAGSDRVMVSPLAVTWWNRNGPMTSTVHYPKIYKTYFEKVERLKHGTFGPVHFRNQVK

>A|CY083917|A/Aalborg/INS132/2009
MERIKELRDLMSQSRTREILTKTTVDHMAIIKKYTSGRQEKNPALRMKWMMAMRYPITADKRIMDMIPER"""


@pytest.fixture
def test_output_data_advanced():
    return [
        {'position': 1, 'entropy': 1.5840926664445014, 'variants_flattened': ['MERIKELRN', 'NEQGQTLWS', 'MERIKELRD'],
         'supports': 3, 'variants': [
            {'position': 1, 'sequence': 'MERIKELRN', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 1, 'sequence': 'NEQGQTLWS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 1, 'sequence': 'MERIKELRD', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['MERIKELRN', 'NEQGQTLWS', 'MERIKELRD']}},
        {'position': 2, 'entropy': 1.5847149221039536, 'variants_flattened': ['ERIKELRNL', 'EQGQTLWSK', 'ERIKELRDL'],
         'supports': 3, 'variants': [
            {'position': 2, 'sequence': 'ERIKELRNL', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 2, 'sequence': 'EQGQTLWSK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 2, 'sequence': 'ERIKELRDL', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['ERIKELRNL', 'EQGQTLWSK', 'ERIKELRDL']}},
        {'position': 3, 'entropy': 1.5852770999375254, 'variants_flattened': ['RIKELRNLM', 'QGQTLWSKM', 'RIKELRDLM'],
         'supports': 3, 'variants': [
            {'position': 3, 'sequence': 'RIKELRNLM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 3, 'sequence': 'QGQTLWSKM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 3, 'sequence': 'RIKELRDLM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['RIKELRNLM', 'QGQTLWSKM', 'RIKELRDLM']}},
        {'position': 4, 'entropy': 1.584797835636367, 'variants_flattened': ['IKELRNLMS', 'GQTLWSKMN', 'IKELRDLMS'],
         'supports': 3, 'variants': [
            {'position': 4, 'sequence': 'IKELRNLMS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 4, 'sequence': 'GQTLWSKMN', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 4, 'sequence': 'IKELRDLMS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['IKELRNLMS', 'GQTLWSKMN', 'IKELRDLMS']}},
        {'position': 5, 'entropy': 1.5827085182811584, 'variants_flattened': ['KELRNLMSQ', 'QTLWSKMND', 'KELRDLMSQ'],
         'supports': 3, 'variants': [
            {'position': 5, 'sequence': 'KELRNLMSQ', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 5, 'sequence': 'QTLWSKMND', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 5, 'sequence': 'KELRDLMSQ', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['KELRNLMSQ', 'QTLWSKMND', 'KELRDLMSQ']}},
        {'position': 6, 'entropy': 1.5851386890027535, 'variants_flattened': ['ELRNLMSQS', 'TLWSKMNDA', 'ELRDLMSQS'],
         'supports': 3, 'variants': [
            {'position': 6, 'sequence': 'ELRNLMSQS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 6, 'sequence': 'TLWSKMNDA', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 6, 'sequence': 'ELRDLMSQS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['ELRNLMSQS', 'TLWSKMNDA', 'ELRDLMSQS']}},
        {'position': 7, 'entropy': 1.5843768391164155, 'variants_flattened': ['LRNLMSQSR', 'LWSKMNDAG', 'LRDLMSQSR'],
         'supports': 3, 'variants': [
            {'position': 7, 'sequence': 'LRNLMSQSR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 7, 'sequence': 'LWSKMNDAG', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 7, 'sequence': 'LRDLMSQSR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['LRNLMSQSR', 'LWSKMNDAG', 'LRDLMSQSR']}},
        {'position': 8, 'entropy': 1.5846752609499983, 'variants_flattened': ['RNLMSQSRT', 'WSKMNDAGS', 'RDLMSQSRT'],
         'supports': 3, 'variants': [
            {'position': 8, 'sequence': 'RNLMSQSRT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 8, 'sequence': 'WSKMNDAGS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 8, 'sequence': 'RDLMSQSRT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['RNLMSQSRT', 'WSKMNDAGS', 'RDLMSQSRT']}},
        {'position': 9, 'entropy': 1.5846512464693476, 'variants_flattened': ['NLMSQSRTR', 'SKMNDAGSD', 'DLMSQSRTR'],
         'supports': 3, 'variants': [
            {'position': 9, 'sequence': 'NLMSQSRTR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 9, 'sequence': 'SKMNDAGSD', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 9, 'sequence': 'DLMSQSRTR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['NLMSQSRTR', 'SKMNDAGSD', 'DLMSQSRTR']}},
        {'position': 10, 'entropy': 0.9156816492464478, 'variants_flattened': ['LMSQSRTRE', 'LMSQSRTRE', 'KMNDAGSDR'],
         'supports': 3, 'variants': [
            {'position': 10, 'sequence': 'LMSQSRTRE', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 10, 'sequence': 'KMNDAGSDR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['KMNDAGSDR']}},
        {'position': 11, 'entropy': 0.9112338667375646, 'variants_flattened': ['MSQSRTREI', 'MSQSRTREI', 'MNDAGSDRV'],
         'supports': 3, 'variants': [
            {'position': 11, 'sequence': 'MSQSRTREI', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 11, 'sequence': 'MNDAGSDRV', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['MNDAGSDRV']}},
        {'position': 12, 'entropy': 0.9147429285891074, 'variants_flattened': ['SQSRTREIL', 'SQSRTREIL', 'NDAGSDRVM'],
         'supports': 3, 'variants': [
            {'position': 12, 'sequence': 'SQSRTREIL', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 12, 'sequence': 'NDAGSDRVM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['NDAGSDRVM']}},
        {'position': 13, 'entropy': 0.9167300347011428, 'variants_flattened': ['QSRTREILT', 'QSRTREILT', 'DAGSDRVMV'],
         'supports': 3, 'variants': [
            {'position': 13, 'sequence': 'QSRTREILT', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 13, 'sequence': 'DAGSDRVMV', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['DAGSDRVMV']}},
        {'position': 14, 'entropy': 0.9141909659937554, 'variants_flattened': ['SRTREILTK', 'SRTREILTK', 'AGSDRVMVS'],
         'supports': 3, 'variants': [
            {'position': 14, 'sequence': 'SRTREILTK', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 14, 'sequence': 'AGSDRVMVS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['AGSDRVMVS']}},
        {'position': 15, 'entropy': 0.9216471924252021, 'variants_flattened': ['RTREILTKT', 'RTREILTKT', 'GSDRVMVSP'],
         'supports': 3, 'variants': [
            {'position': 15, 'sequence': 'RTREILTKT', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 15, 'sequence': 'GSDRVMVSP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['GSDRVMVSP']}},
        {'position': 16, 'entropy': 0.9261375977548566, 'variants_flattened': ['TREILTKTT', 'TREILTKTT', 'SDRVMVSPL'],
         'supports': 3, 'variants': [
            {'position': 16, 'sequence': 'TREILTKTT', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 16, 'sequence': 'SDRVMVSPL', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['SDRVMVSPL']}},
        {'position': 17, 'entropy': 0.9192482724735207, 'variants_flattened': ['REILTKTTV', 'REILTKTTV', 'DRVMVSPLA'],
         'supports': 3, 'variants': [
            {'position': 17, 'sequence': 'REILTKTTV', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 17, 'sequence': 'DRVMVSPLA', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['DRVMVSPLA']}},
        {'position': 18, 'entropy': 0.9185392771642034, 'variants_flattened': ['EILTKTTVD', 'EILTKTTVD', 'RVMVSPLAV'],
         'supports': 3, 'variants': [
            {'position': 18, 'sequence': 'EILTKTTVD', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 18, 'sequence': 'RVMVSPLAV', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['RVMVSPLAV']}},
        {'position': 19, 'entropy': 0.9137129773039376, 'variants_flattened': ['ILTKTTVDH', 'ILTKTTVDH', 'VMVSPLAVT'],
         'supports': 3, 'variants': [
            {'position': 19, 'sequence': 'ILTKTTVDH', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 19, 'sequence': 'VMVSPLAVT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['VMVSPLAVT']}},
        {'position': 20, 'entropy': 0.9149822067876137, 'variants_flattened': ['LTKTTVDHM', 'LTKTTVDHM', 'MVSPLAVTW'],
         'supports': 3, 'variants': [
            {'position': 20, 'sequence': 'LTKTTVDHM', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 20, 'sequence': 'MVSPLAVTW', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['MVSPLAVTW']}},
        {'position': 21, 'entropy': 0.9194544591906372, 'variants_flattened': ['TKTTVDHMA', 'TKTTVDHMA', 'VSPLAVTWW'],
         'supports': 3, 'variants': [
            {'position': 21, 'sequence': 'TKTTVDHMA', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 21, 'sequence': 'VSPLAVTWW', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['VSPLAVTWW']}},
        {'position': 22, 'entropy': 0.9219824366283061, 'variants_flattened': ['KTTVDHMAI', 'KTTVDHMAI', 'SPLAVTWWN'],
         'supports': 3, 'variants': [
            {'position': 22, 'sequence': 'KTTVDHMAI', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 22, 'sequence': 'SPLAVTWWN', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['SPLAVTWWN']}},
        {'position': 23, 'entropy': 0.9202880602415983, 'variants_flattened': ['TTVDHMAII', 'TTVDHMAII', 'PLAVTWWNR'],
         'supports': 3, 'variants': [
            {'position': 23, 'sequence': 'TTVDHMAII', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 23, 'sequence': 'PLAVTWWNR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['PLAVTWWNR']}},
        {'position': 24, 'entropy': 0.9156228336665766, 'variants_flattened': ['TVDHMAIIK', 'TVDHMAIIK', 'LAVTWWNRN'],
         'supports': 3, 'variants': [
            {'position': 24, 'sequence': 'TVDHMAIIK', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 24, 'sequence': 'LAVTWWNRN', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['LAVTWWNRN']}},
        {'position': 25, 'entropy': 0.9155428539611046, 'variants_flattened': ['VDHMAIIKK', 'VDHMAIIKK', 'AVTWWNRNG'],
         'supports': 3, 'variants': [
            {'position': 25, 'sequence': 'VDHMAIIKK', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 25, 'sequence': 'AVTWWNRNG', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['AVTWWNRNG']}},
        {'position': 26, 'entropy': 0.9155634156823506, 'variants_flattened': ['DHMAIIKKY', 'DHMAIIKKY', 'VTWWNRNGP'],
         'supports': 3, 'variants': [
            {'position': 26, 'sequence': 'DHMAIIKKY', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 26, 'sequence': 'VTWWNRNGP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['VTWWNRNGP']}},
        {'position': 27, 'entropy': 0.9230316242917805, 'variants_flattened': ['HMAIIKKYT', 'HMAIIKKYT', 'TWWNRNGPM'],
         'supports': 3, 'variants': [
            {'position': 27, 'sequence': 'HMAIIKKYT', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 27, 'sequence': 'TWWNRNGPM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['TWWNRNGPM']}},
        {'position': 28, 'entropy': 0.9182451021665898, 'variants_flattened': ['MAIIKKYTS', 'MAIIKKYTS', 'WWNRNGPMT'],
         'supports': 3, 'variants': [
            {'position': 28, 'sequence': 'MAIIKKYTS', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 28, 'sequence': 'WWNRNGPMT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['WWNRNGPMT']}},
        {'position': 29, 'entropy': 0.9197736091431303, 'variants_flattened': ['AIIKKYTSG', 'AIIKKYTSG', 'WNRNGPMTS'],
         'supports': 3, 'variants': [
            {'position': 29, 'sequence': 'AIIKKYTSG', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 29, 'sequence': 'WNRNGPMTS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['WNRNGPMTS']}},
        {'position': 30, 'entropy': 0.9221826376953125, 'variants_flattened': ['IIKKYTSGR', 'IIKKYTSGR', 'NRNGPMTST'],
         'supports': 3, 'variants': [
            {'position': 30, 'sequence': 'IIKKYTSGR', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 30, 'sequence': 'NRNGPMTST', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['NRNGPMTST']}},
        {'position': 31, 'entropy': 0.9214429167730588, 'variants_flattened': ['IKKYTSGRQ', 'IKKYTSGRQ', 'RNGPMTSTV'],
         'supports': 3, 'variants': [
            {'position': 31, 'sequence': 'IKKYTSGRQ', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 31, 'sequence': 'RNGPMTSTV', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['RNGPMTSTV']}},
        {'position': 32, 'entropy': 0.911064196366588, 'variants_flattened': ['KKYTSGRQE', 'KKYTSGRQE', 'NGPMTSTVH'],
         'supports': 3, 'variants': [
            {'position': 32, 'sequence': 'KKYTSGRQE', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 32, 'sequence': 'NGPMTSTVH', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['NGPMTSTVH']}},
        {'position': 33, 'entropy': 0.917361917353838, 'variants_flattened': ['KYTSGRQEK', 'KYTSGRQEK', 'GPMTSTVHY'],
         'supports': 3, 'variants': [
            {'position': 33, 'sequence': 'KYTSGRQEK', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 33, 'sequence': 'GPMTSTVHY', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['GPMTSTVHY']}},
        {'position': 34, 'entropy': 0.9239296596114006, 'variants_flattened': ['YTSGRQEKN', 'YTSGRQEKN', 'PMTSTVHYP'],
         'supports': 3, 'variants': [
            {'position': 34, 'sequence': 'YTSGRQEKN', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 34, 'sequence': 'PMTSTVHYP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['PMTSTVHYP']}},
        {'position': 35, 'entropy': 0.9234206137735347, 'variants_flattened': ['TSGRQEKNP', 'TSGRQEKNP', 'MTSTVHYPK'],
         'supports': 3, 'variants': [
            {'position': 35, 'sequence': 'TSGRQEKNP', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 35, 'sequence': 'MTSTVHYPK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['MTSTVHYPK']}},
        {'position': 36, 'entropy': 1.5846246063986256, 'variants_flattened': ['SGRQEKNPS', 'TSTVHYPKI', 'SGRQEKNPA'],
         'supports': 3, 'variants': [
            {'position': 36, 'sequence': 'SGRQEKNPS', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 36, 'sequence': 'TSTVHYPKI', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 36, 'sequence': 'SGRQEKNPA', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['SGRQEKNPS', 'TSTVHYPKI', 'SGRQEKNPA']}},
        {'position': 37, 'entropy': 1.584717362150843, 'variants_flattened': ['GRQEKNPSL', 'STVHYPKIY', 'GRQEKNPAL'],
         'supports': 3, 'variants': [
            {'position': 37, 'sequence': 'GRQEKNPSL', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 37, 'sequence': 'STVHYPKIY', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 37, 'sequence': 'GRQEKNPAL', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['GRQEKNPSL', 'STVHYPKIY', 'GRQEKNPAL']}},
        {'position': 38, 'entropy': 1.5846235664746342, 'variants_flattened': ['RQEKNPSLR', 'TVHYPKIYK', 'RQEKNPALR'],
         'supports': 3, 'variants': [
            {'position': 38, 'sequence': 'RQEKNPSLR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 38, 'sequence': 'TVHYPKIYK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 38, 'sequence': 'RQEKNPALR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['RQEKNPSLR', 'TVHYPKIYK', 'RQEKNPALR']}},
        {'position': 39, 'entropy': 1.5850413738923923, 'variants_flattened': ['QEKNPSLRM', 'VHYPKIYKT', 'QEKNPALRM'],
         'supports': 3, 'variants': [
            {'position': 39, 'sequence': 'QEKNPSLRM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 39, 'sequence': 'VHYPKIYKT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 39, 'sequence': 'QEKNPALRM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['QEKNPSLRM', 'VHYPKIYKT', 'QEKNPALRM']}},
        {'position': 40, 'entropy': 1.5847804646554857, 'variants_flattened': ['EKNPSLRMK', 'HYPKIYKTY', 'EKNPALRMK'],
         'supports': 3, 'variants': [
            {'position': 40, 'sequence': 'EKNPSLRMK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 40, 'sequence': 'HYPKIYKTY', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 40, 'sequence': 'EKNPALRMK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['EKNPSLRMK', 'HYPKIYKTY', 'EKNPALRMK']}},
        {'position': 41, 'entropy': 1.5848699669298885, 'variants_flattened': ['KNPSLRMKW', 'YPKIYKTYF', 'KNPALRMKW'],
         'supports': 3, 'variants': [
            {'position': 41, 'sequence': 'KNPSLRMKW', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 41, 'sequence': 'YPKIYKTYF', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 41, 'sequence': 'KNPALRMKW', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['KNPSLRMKW', 'YPKIYKTYF', 'KNPALRMKW']}},
        {'position': 42, 'entropy': 1.5848712138230496, 'variants_flattened': ['NPSLRMKWM', 'PKIYKTYFE', 'NPALRMKWM'],
         'supports': 3, 'variants': [
            {'position': 42, 'sequence': 'NPSLRMKWM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 42, 'sequence': 'PKIYKTYFE', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 42, 'sequence': 'NPALRMKWM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['NPSLRMKWM', 'PKIYKTYFE', 'NPALRMKWM']}},
        {'position': 43, 'entropy': 1.5847032999363075, 'variants_flattened': ['PSLRMKWMM', 'KIYKTYFEK', 'PALRMKWMM'],
         'supports': 3, 'variants': [
            {'position': 43, 'sequence': 'PSLRMKWMM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 43, 'sequence': 'KIYKTYFEK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 43, 'sequence': 'PALRMKWMM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['PSLRMKWMM', 'KIYKTYFEK', 'PALRMKWMM']}},
        {'position': 44, 'entropy': 1.5851699921428168, 'variants_flattened': ['SLRMKWMMA', 'IYKTYFEKV', 'ALRMKWMMA'],
         'supports': 3, 'variants': [
            {'position': 44, 'sequence': 'SLRMKWMMA', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 44, 'sequence': 'IYKTYFEKV', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 44, 'sequence': 'ALRMKWMMA', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['SLRMKWMMA', 'IYKTYFEKV', 'ALRMKWMMA']}},
        {'position': 45, 'entropy': 0.918210546417874, 'variants_flattened': ['LRMKWMMAM', 'LRMKWMMAM', 'YKTYFEKVE'],
         'supports': 3, 'variants': [
            {'position': 45, 'sequence': 'LRMKWMMAM', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 45, 'sequence': 'YKTYFEKVE', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['YKTYFEKVE']}},
        {'position': 46, 'entropy': 1.5848746784111045, 'variants_flattened': ['RMKWMMAMK', 'KTYFEKVER', 'RMKWMMAMR'],
         'supports': 3, 'variants': [
            {'position': 46, 'sequence': 'RMKWMMAMK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 46, 'sequence': 'KTYFEKVER', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 46, 'sequence': 'RMKWMMAMR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['RMKWMMAMK', 'KTYFEKVER', 'RMKWMMAMR']}},
        {'position': 47, 'entropy': 1.584952852663701, 'variants_flattened': ['MKWMMAMKY', 'TYFEKVERL', 'MKWMMAMRY'],
         'supports': 3, 'variants': [
            {'position': 47, 'sequence': 'MKWMMAMKY', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 47, 'sequence': 'TYFEKVERL', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 47, 'sequence': 'MKWMMAMRY', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['MKWMMAMKY', 'TYFEKVERL', 'MKWMMAMRY']}},
        {'position': 48, 'entropy': 1.5848665748830821, 'variants_flattened': ['KWMMAMKYP', 'YFEKVERLK', 'KWMMAMRYP'],
         'supports': 3, 'variants': [
            {'position': 48, 'sequence': 'KWMMAMKYP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 48, 'sequence': 'YFEKVERLK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 48, 'sequence': 'KWMMAMRYP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['KWMMAMKYP', 'YFEKVERLK', 'KWMMAMRYP']}},
        {'position': 49, 'entropy': 1.5850631453201673, 'variants_flattened': ['WMMAMKYPI', 'FEKVERLKH', 'WMMAMRYPI'],
         'supports': 3, 'variants': [
            {'position': 49, 'sequence': 'WMMAMKYPI', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 49, 'sequence': 'FEKVERLKH', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 49, 'sequence': 'WMMAMRYPI', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['WMMAMKYPI', 'FEKVERLKH', 'WMMAMRYPI']}},
        {'position': 50, 'entropy': 1.5851179651289706, 'variants_flattened': ['MMAMKYPIT', 'EKVERLKHG', 'MMAMRYPIT'],
         'supports': 3, 'variants': [
            {'position': 50, 'sequence': 'MMAMKYPIT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 50, 'sequence': 'EKVERLKHG', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 50, 'sequence': 'MMAMRYPIT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['MMAMKYPIT', 'EKVERLKHG', 'MMAMRYPIT']}},
        {'position': 51, 'entropy': 1.5847268484932595, 'variants_flattened': ['MAMKYPITA', 'KVERLKHGT', 'MAMRYPITA'],
         'supports': 3, 'variants': [
            {'position': 51, 'sequence': 'MAMKYPITA', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 51, 'sequence': 'KVERLKHGT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 51, 'sequence': 'MAMRYPITA', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['MAMKYPITA', 'KVERLKHGT', 'MAMRYPITA']}},
        {'position': 52, 'entropy': 1.5848764509770787, 'variants_flattened': ['AMKYPITAD', 'VERLKHGTF', 'AMRYPITAD'],
         'supports': 3, 'variants': [
            {'position': 52, 'sequence': 'AMKYPITAD', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 52, 'sequence': 'VERLKHGTF', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 52, 'sequence': 'AMRYPITAD', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['AMKYPITAD', 'VERLKHGTF', 'AMRYPITAD']}},
        {'position': 53, 'entropy': 1.5844367299000295, 'variants_flattened': ['MKYPITADK', 'ERLKHGTFG', 'MRYPITADK'],
         'supports': 3, 'variants': [
            {'position': 53, 'sequence': 'MKYPITADK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 53, 'sequence': 'ERLKHGTFG', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 53, 'sequence': 'MRYPITADK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['MKYPITADK', 'ERLKHGTFG', 'MRYPITADK']}},
        {'position': 54, 'entropy': 1.5849536130577706, 'variants_flattened': ['KYPITADKR', 'RLKHGTFGP', 'RYPITADKR'],
         'supports': 3, 'variants': [
            {'position': 54, 'sequence': 'KYPITADKR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 54, 'sequence': 'RLKHGTFGP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 54, 'sequence': 'RYPITADKR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['KYPITADKR', 'RLKHGTFGP', 'RYPITADKR']}},
        {'position': 55, 'entropy': 0.9190646445200947, 'variants_flattened': ['YPITADKRI', 'YPITADKRI', 'LKHGTFGPV'],
         'supports': 3, 'variants': [
            {'position': 55, 'sequence': 'YPITADKRI', 'count': 2, 'incidence': 66.66666666666667, 'motif_short': 'I',
             'motif_long': 'Index', 'type': ['A', 'A'], 'accession': ['CY021716', 'CY083917'],
             'strain': ['A/AA/Huston/1945', 'A/Aalborg/INS132/2009'], 'country': ['USA', 'Denmark']},
            {'position': 55, 'sequence': 'LKHGTFGPV', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']}], 'kmer_types': {'incidence': 33.33333333333333, 'types': ['LKHGTFGPV']}},
        {'position': 56, 'entropy': 1.5845029205433776, 'variants_flattened': ['PITADKRIT', 'KHGTFGPVH', 'PITADKRIM'],
         'supports': 3, 'variants': [
            {'position': 56, 'sequence': 'PITADKRIT', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 56, 'sequence': 'KHGTFGPVH', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 56, 'sequence': 'PITADKRIM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['PITADKRIT', 'KHGTFGPVH', 'PITADKRIM']}},
        {'position': 57, 'entropy': 1.585054253865224, 'variants_flattened': ['ITADKRITE', 'HGTFGPVHF', 'ITADKRIMD'],
         'supports': 3, 'variants': [
            {'position': 57, 'sequence': 'ITADKRITE', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 57, 'sequence': 'HGTFGPVHF', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 57, 'sequence': 'ITADKRIMD', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['ITADKRITE', 'HGTFGPVHF', 'ITADKRIMD']}},
        {'position': 58, 'entropy': 1.5846020583415295, 'variants_flattened': ['TADKRITEM', 'GTFGPVHFR', 'TADKRIMDM'],
         'supports': 3, 'variants': [
            {'position': 58, 'sequence': 'TADKRITEM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 58, 'sequence': 'GTFGPVHFR', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 58, 'sequence': 'TADKRIMDM', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['TADKRITEM', 'GTFGPVHFR', 'TADKRIMDM']}},
        {'position': 59, 'entropy': 1.5851255617547702, 'variants_flattened': ['ADKRITEMI', 'TFGPVHFRN', 'ADKRIMDMI'],
         'supports': 3, 'variants': [
            {'position': 59, 'sequence': 'ADKRITEMI', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 59, 'sequence': 'TFGPVHFRN', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 59, 'sequence': 'ADKRIMDMI', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['ADKRITEMI', 'TFGPVHFRN', 'ADKRIMDMI']}},
        {'position': 60, 'entropy': 1.5848592154869867, 'variants_flattened': ['DKRITEMIP', 'FGPVHFRNQ', 'DKRIMDMIP'],
         'supports': 3, 'variants': [
            {'position': 60, 'sequence': 'DKRITEMIP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 60, 'sequence': 'FGPVHFRNQ', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 60, 'sequence': 'DKRIMDMIP', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['DKRITEMIP', 'FGPVHFRNQ', 'DKRIMDMIP']}},
        {'position': 61, 'entropy': 1.5848955623221177, 'variants_flattened': ['KRITEMIPE', 'GPVHFRNQV', 'KRIMDMIPE'],
         'supports': 3, 'variants': [
            {'position': 61, 'sequence': 'KRITEMIPE', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 61, 'sequence': 'GPVHFRNQV', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 61, 'sequence': 'KRIMDMIPE', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['KRITEMIPE', 'GPVHFRNQV', 'KRIMDMIPE']}},
        {'position': 62, 'entropy': 1.5861148896902224, 'variants_flattened': ['RITEMIPER', 'PVHFRNQVK', 'RIMDMIPER'],
         'supports': 3, 'variants': [
            {'position': 62, 'sequence': 'RITEMIPER', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY021716'], 'strain': ['A/AA/Huston/1945'],
             'country': ['USA']},
            {'position': 62, 'sequence': 'PVHFRNQVK', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY020292'], 'strain': ['A/AA/Marton/1943'],
             'country': ['USA']},
            {'position': 62, 'sequence': 'RIMDMIPER', 'count': 1, 'incidence': 33.333333333333336, 'motif_short': 'U',
             'motif_long': 'Unique', 'type': ['A'], 'accession': ['CY083917'], 'strain': ['A/Aalborg/INS132/2009'],
             'country': ['Denmark']}],
         'kmer_types': {'incidence': 66.66666666666666, 'types': ['RITEMIPER', 'PVHFRNQVK', 'RIMDMIPER']}}]


def test_run_module_advanced(test_input_data_advanced, test_output_data_advanced):
    from hunana import Hunana
    handle = StringIO(test_input_data_advanced)

    results = Hunana(handle, header_decode=True, header_format='(type)|(accession)|(strain)|(country)').run()

    for results, test in zip(results, test_output_data_advanced):
        assert results.get('position') == test.get('position')
        assert results.get('supports') == test.get('supports')
        assert results.get('variants') == test.get('variants')
        assert results.get('kmer_types') == test.get('kmer_types')


def test_run_module_advanced_no_format(test_input_data_advanced):
    from hunana import Hunana
    from hunana.errorhandlers.exceptions import NoHeaderFormat

    handle = StringIO(test_input_data_advanced)

    with pytest.raises(NoHeaderFormat):
        Hunana(handle, header_decode=True).run()


def test_run_module_advanced_empty_header_data_fail(test_input_data_advanced_missing_header_items):
    from hunana import Hunana
    from hunana.errorhandlers.exceptions import HeaderItemEmpty

    handle = StringIO(test_input_data_advanced_missing_header_items)

    with pytest.raises(HeaderItemEmpty):
        Hunana(handle, header_decode=True, header_format='(type)|(accession)|(strain)|(country)').run()


def test_run_module_advanced_empty_header_data_success(test_input_data_advanced_missing_header_items):
    from hunana import Hunana

    handle = StringIO(test_input_data_advanced_missing_header_items)

    Hunana(handle, header_decode=True, header_format='(type)|(accession)|(strain)|(country)',
           no_header_error=True).run()


def test_run_module_advanced_header_item_count_invalid(test_input_data_advanced_item_count_invalid):
    from hunana import Hunana
    from hunana.errorhandlers.exceptions import HeaderItemCountInvalid

    handle1 = StringIO(test_input_data_advanced_item_count_invalid)
    handle2 = StringIO(test_input_data_advanced_item_count_invalid)

    with pytest.raises(HeaderItemCountInvalid):
        Hunana(handle1, header_decode=True, header_format='(type)|(accession)|(strain)|(country)',
               no_header_error=True).run()

    with pytest.raises(HeaderItemCountInvalid):
        Hunana(handle2, header_decode=True, header_format='(type)|(accession)|(strain)|(country)').run()


def test_run_cli_advanced(test_input_data_advanced, test_output_data_advanced):
    process = subprocess.run(['hunana', '-he', '-f', '(type)|(accession)|(strain)|(country)'],
                             input=test_input_data_advanced.encode('utf-8'), stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

    assert process.returncode == 0

    results = loads(process.stdout.decode('utf-8'))

    for results, test in zip(results, test_output_data_advanced):
        assert results.get('position') == test.get('position')
        assert results.get('supports') == test.get('supports')
        assert results.get('variants') == test.get('variants')
        assert results.get('kmer_types') == test.get('kmer_types')
