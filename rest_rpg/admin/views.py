from flask.ext.superadmin import BaseView, expose


class MyView(BaseView):

	@expose("/")
	def admin_index(self):
		return self.render("admin/index.html")

	def __repr__(self):
		pass