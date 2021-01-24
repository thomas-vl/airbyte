import React from "react";
import { FormattedMessage } from "react-intl";

export const createFormErrorMessage = (status?: number, message?: string) => {
  if (message) {
    return message;
  }

  if (!status || status === 0) {
    return null;
  }
  return status === 400 ? (
    <FormattedMessage id="form.validationError" />
  ) : (
    <FormattedMessage id="form.someError" />
  );
};
