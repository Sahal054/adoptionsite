from flask import Flask, url_for, render_template, redirect, Blueprint
from adoptionsite import db
from adoptionsite.models import Puppies
from adoptionsite.models import Owner
from adoptionsite.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint(
    'puppy', __name__, template_folder='templates/puppies',static_folder='static')


@puppies_blueprint.route('/add', methods=["GET", "POST"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        new = Puppies(name)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('puppy.list_pup'))

    return render_template('add.html', form=form)


@puppies_blueprint.route('/list', methods=["GET", "POST"])
def list_pup():
    pups = Puppies.query.all()
    owns = Owner.query.all()

    return render_template('list.html', pups=pups,owns=owns)


@puppies_blueprint.route('/delete', methods=["GET", "POST"])
def remove_pup():
    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppies.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for("puppy.list_pup"))

    return render_template("delete.html", form=form)
