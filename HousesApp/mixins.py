
class UserOwnsHouseMixin(UserPassesTestMixin):
    
    def test_func(self):
        current_listing_creator = self.get_object().create_by_user
        requesting_user = self.request.user
        return requesting_user == current_listing_creator