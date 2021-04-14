"""
"""
import mne
from surfer import Brain

from simoparc import AdaptiveParcellation

data_path = mne.datasets.sample.data_path()
subjects_dir = data_path + '/subjects'
subject = 'sample'

# read forward solution
fname_fwd = data_path + '/MEG/sample/sample_audvis-meg-oct-6-fwd.fif'
fwd = mne.read_forward_solution(fname_fwd)

# read inverse solution
fname_inv = data_path + '/MEG/sample/sample_audvis-meg-oct-6-meg-inv.fif'
inv = mne.minimum_norm.read_inverse_operator(fname_inv)

# create and save parcellation
parc = AdaptiveParcellation('simoparc', subject=subject,
                            subjects_dir=subjects_dir, hemi='both')
parc.fit(fwd, inv)
parc.save_annot(overwrite=True)

# create brain for plotting
brain = Brain(subject, 'both', 'inflated', subjects_dir=subjects_dir, alpha=0.999)

# add all labels to plot in one go from annotation file
brain.add_annotation('simoparc')
