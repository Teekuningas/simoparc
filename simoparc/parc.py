"""
"""
import mne


class AdaptiveParcellation:
    """
    """
    def __init__(self, name, distance='angle', hemi='both',
                 subject='fsaverage', subjects_dir=None):
        """
        """
        self.name = name
        self.distance = distance
        self.hemi = hemi
        self.subject = subject
        self.subjects_dir = subjects_dir

        self.labels = None

    def fit(self, fwd, inv):
        """
        """
        self.labels = adaptive_parcellation(fwd, inv, self.distance)

    def fit_transform(self, fwd, inv):
        """
        """
        self.labels = adaptive_parcellation(fwd, inv, self.distance)
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


def adaptive_parcellation(fwd, inv, distance='angle', hemi='both'):
    """ 
    """
    labels = []

    # Magic happens
    # res = mne.minimum_norm.make_inverse_resolution_matrix(fwd, inv)
    # ...

    # In the meanwhile, create a dummy
    vertices = inv['src'][0]['vertno'][:int(len(inv['src'][0]['vertno'])/2)]
    labels.append(mne.Label(vertices, hemi='lh', name='1'))

    return labels

