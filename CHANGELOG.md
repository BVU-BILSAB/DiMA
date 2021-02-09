# CHANGE LOG

## 2021/02/09

### Added
* Now can be installed via pip install.

### Changed

### Fixed

## 2021/01/31

### Added
* Entropy now calculated by default.
* Details for each variant can now be generated from the fasta header using the flags -he and -f.

### Changed

### Fixed

## 2021/01/23

### Added
* Results will now be sent to stdout when no output file (--output/-o) is specified. All errors sent to stderr.
* Added CHANGELOG.md where all future changes will be logged.

### Changed

### Fixed
* Show the number of variants at each position (supports). (Thanks Muhammet)

## 2021/01/15

### Added

### Changed

### Fixed
* Fixed issue where kmer positions with atleast one invalid character in all variants were skipped (Thanks for catching this issue Muhammet!).
