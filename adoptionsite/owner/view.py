from flask import Flask, url_for, render_template, redirect,Blueprint
from adoptionsite import db
from adoptionsite.models import Owner
from adoptionsite.owner.forms import AddForm


owners_blueprint=Blueprint('owner',__name__,template_folder='templates/owner',static_folder='static')


@owners_blueprint.route('/add',methods=["GET","POST"])
def add():
    form=AddForm()

    if form.validate_on_submit():
        name= form.name.data
        pup_id=form.id.data
        new_owner=Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('puppy.list_pup'))
    return render_template('owner.html',form=form)
