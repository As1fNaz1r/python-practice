try:
    pass
except (ValueError, TyypeError, KeyError) as e:
    print(f"Error occured: {e}")