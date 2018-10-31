from flask import Blueprint, render_template

landscape = Blueprint(
  'landscape', __name__,
  template_folder='/templates', static_folder='/static')

@landscape.route('/')
def index():
    return render_template('landscape/index.html')


@landscape.route('/landscape-features')
def landscape_features():
    return render_template('landscape/landscape-features.html')


@landscape.route('/try-landscape')
def try_landscape():
    return render_template('landscape/try-landscape.html')


@landscape.route('/set-up-on-prem')
def set_up_on_prem():
    return render_template('landscape/set-up-on-prem.html')


@landscape.route('/_status/check')
def health_check():
    """ Health check end point used by Talisker.
    """
    return ('', 200)
