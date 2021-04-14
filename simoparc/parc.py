"""
"""
import mne
import numpy as np


class AdaptiveParcellation:
    """
    """
    def __init__(self, name, hemi='both',
                 subject='fsaverage', subjects_dir=None):
        """
        """
        self.name = name
        self.hemi = hemi
        self.subject = subject
        self.subjects_dir = subjects_dir

        self.labels = None

    def fit(self, fwd, inv):
        """
        """
        self.labels = adaptive_parcellation(fwd, inv, self.subject, self.subjects_dir)

    def fit_transform(self, fwd, inv):
        """
        """
        self.labels = adaptive_parcellation(fwd, inv, self.subject, self.subjects_dir)
        return self.labels

    def plot_dendrogram(self, ax=None):
        """
        """
        if not self.labels:
            raise Exception('To plot dendrogram, you must fit first')

    def save_annot(self, overwrite=False):
        """
        """
        if not self.labels:
            raise Exception('To save annot, you must fit first')

        mne.write_labels_to_annot(
            self.labels, subject=self.subject, hemi=self.hemi,
            parc=self.name, subjects_dir=self.subjects_dir,
            overwrite=overwrite)


def adaptive_parcellation(fwd, inv, subject, subjects_dir, hemi='both'):
    """ 
    """
    # Magic happens
    # res = mne.minimum_norm.make_inverse_resolution_matrix(fwd, inv)
    # ...

    # However, here's a magicless example
    labels_aparc = mne.read_labels_from_annot(subject, parc='aparc', hemi='lh', 
                                              subjects_dir=subjects_dir)

    # add frontal pole label to lh
    vertices = labels_aparc[5].vertices
    label1 = mne.Label(vertices, hemi='lh', name='frontalpole', 
                       subject=subject, color=(1,0,0,1))

    # add label of rightmost vertices to rh
    vertices = inv['src'][1]['vertno']
    vertices = [vv for vv in vertices if inv['src'][1]['rr'][vv, 0] > 0.05]
    label2 = mne.Label(vertices, hemi='rh', name='lateral', 
                       subject=subject, color=(0,1,0,1))
    label2 = label2.fill(inv['src'])

    labels = [label1, label2]
    return labels

