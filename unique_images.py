def unique_file_path(instance, filename):
    # Save original file name in model
    instance.original_file_name = filename

    # Get new file name/upload path
    base, ext = splitext(filename)
    newname = "%s%s" % (uuid.uuid4(), ext)
    return os.path.join('photos', newname)

class Photo(models.Model):
    picture = models.ImageField(upload_to=unique_file_path)

    # editable=false makes it so users can't edit this field
    original_file_name = models.CharField(editable=False, max_length=100) 
