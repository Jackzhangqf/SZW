from  django  import  template
register  =  template.Library()
@register.simple_tag
def  get_verbose_name(qqq):
	return  qqq.model._meta.verbose_name_plural
